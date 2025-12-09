// simple upload helper for Desk or Website
function gdevelop_upload(form) {
var data = new FormData(form);
fetch('/api/resource/GDevelop%20Game', {
method: 'POST',
body: data,
credentials: 'include'
}).then(r=>r.json()).then(resp=>{
if (resp.data) {
alert('Game created: ' + resp.data.name + '. Please attach ZIP in the record and Save to deploy.');
window.location = '/app/gdevelop-game/' + resp.data.name;
} else {
alert('Error: ' + JSON.stringify(resp));
}
})
}
