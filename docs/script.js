const url = 'https://raw.githubusercontent.com/tusharhero/randomlygeneratedytlinks/main/ytrandlinks.json';

fetch(url).then(x => x.json()).then((x) => 
{
    const ytEmbed = document.getElementById('ytEmbed');
    const channelName = document.getElementById('channelName');

    const src = `https://www.youtube-nocookie.com/embed/${x.id.videoID}`;

    ytEmbed.setAttribute('src', src);

    channelName.innerHTML = x.id.channelName;

    ytEmbed.style.visibility = 'visible';
});