// For Add to Playlist
document.querySelectorAll('.add-to-playlist').forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        const songname = this.getAttribute('data-title');

        const hiddenForm = document.getElementById('hiddenForm');
        const titleInput = document.getElementById('titleInput');
        titleInput.value = songname;

        hiddenForm.submit();
    });
});

// For Remove from Playlist
function removeSong(songTitle) {
    const removeForm = document.getElementById('removeSongForm');
    const removeInput = document.getElementById('titleInput');
    removeInput.value = songTitle;

    removeForm.submit();
}
