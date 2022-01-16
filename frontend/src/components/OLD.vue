<template>
  <div>
    <form>
        <label for="username">Name: </label>
        <input type="text" name=”username” id="username">
        <label for="username">Room SID: </label>
        <input type="text" name=”sid” id="sid">
        <button id="join_leave" @click='connectButtonHandler'>Join call</button>
    </form>
    <p id="count"></p>
    <div id="container" class="container">
        <div id="local" class="participant"><div></div><div>Me</div></div>
        <!-- more participants will be added dynamically here -->
    </div>
  </div>

        <!-- <script src="//media.twiliocdn.com/sdk/js/video/releases/2.3.0/twilio-video.min.js"></script> -->
</template>


<script>

  // addLocalVideo();
  // button.addEventListener('click', connectButtonHandler);

          //     addLocalVideo() {
        // Twilio.Video.createLocalVideoTrack().then(track => {
        //     let video = document.getElementById('local').firstChild;
        //     video.appendChild(track.attach());
        // }),

  export default {
    name: 'VideoPage',
    data() { 
      return {
        connected : false,
        usernameInput : document.getElementById('username'),
        button : document.getElementById('join_leave'),
        container : document.getElementById('container'),
        count : document.getElementById('count'),
        roomSid : document.getElementById('sid'),
        room: '',
      }
    },
    setup() {
      console.log("something")
      
      Twilio.Video.createLocalVideoTrack().then(track => {
          let video = document.getElementById('local').firstChild;
          video.appendChild(track.attach());
      })
    },

    methods: {
      connectButtonHandler(event) {
          event.preventDefault();
          if (!connected) {
              let username = usernameInput.value;
              if (!username) {
                  alert('Enter your name before connecting');
                  return;
              }
              button.disabled = true;
              button.innerHTML = 'Connecting...';
              connect(username).then(() => {
                  button.innerHTML = 'Leave call';
                  button.disabled = false;
              }).catch(() => {
                  alert('Connection failed. Is the backend running?');
                  button.innerHTML = 'Join call';
                  button.disabled = false;    
              });
          }
          else {
              disconnect();
              button.innerHTML = 'Join call';
              connected = false;
          }
      },
      connect(username) {
          let promise = new Promise((resolve, reject) => {
              // get a token from the back end
              fetch('token', {
                  method: 'POST',
                  body: JSON.stringify({'username': username, 'sid': roomSid.value}),
              }).then(res => res.json()).then(data => {
                  // join video call
                  return Twilio.Video.connect(data.token);
              }).then(_room => {
                  room = _room;
                  room.participants.forEach(participantConnected);
                  room.on('participantConnected', participantConnected);
                  room.on('participantDisconnected', participantDisconnected);
                  connected = true;
                  updateParticipantCount();
                  resolve();
              }).catch(() => {
                  reject();
              });
          });
          return promise;
      },
      updateParticipantCount() {
          if (!connected)
              count.innerHTML = 'Disconnected.';
          else
              count.innerHTML = (room.participants.size + 1) + ' participants online.';
      },
      participantConnected(participant) {
          let participantDiv = document.createElement('div');
          participantDiv.setAttribute('id', participant.sid);
          participantDiv.setAttribute('class', 'participant');

          let tracksDiv = document.createElement('div');
          participantDiv.appendChild(tracksDiv);

          let labelDiv = document.createElement('div');
          labelDiv.innerHTML = participant.identity;
          participantDiv.appendChild(labelDiv);

          container.appendChild(participantDiv);

          participant.tracks.forEach(publication => {
              if (publication.isSubscribed)
                  trackSubscribed(tracksDiv, publication.track);
          });
          participant.on('trackSubscribed', track => trackSubscribed(tracksDiv, track));
          participant.on('trackUnsubscribed', trackUnsubscribed);

          updateParticipantCount();
      },

      participantDisconnected(participant) {
          document.getElementById(participant.sid).remove();
          updateParticipantCount();
      },

      trackSubscribed(div, track) {
          div.appendChild(track.attach());
      },

      trackUnsubscribed(track) {
          track.detach().forEach(element => element.remove());
      },
      disconnect() {
          room.disconnect();
          while (container.lastChild.id != 'local')
              container.removeChild(container.lastChild);
          button.innerHTML = 'Join call';
          connected = false;
          updateParticipantCount();
      },
    }
  }
</script>


<style>

</style>