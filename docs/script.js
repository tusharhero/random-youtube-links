const ytEmbed = document.getElementById('ytEmbed');

const url = 'https://raw.githubusercontent.com/tusharhero/randomlygeneratedytlinks/main/ytrandlinks.json';

fetch(url).then(x => x.json()).then((x) => 
{
    const src = 'https://www.youtube.com/embed/' + x.id.videoID;

    ytEmbed.setAttribute('src', src);

    ytEmbed.style.visibility = 'visible';
});