const loadImage = async (url) => 
    new Promise(resolve=>{
    const img = new Image();
    img.addEventListener("load",
     () => {
        console.log('loaded: '+url);
        return resolve(img);
    });
    img.src = url;
    console.log('loading img: '+url)
});

const loadAudio = async(path)=>new Promise(resolve=>{
    const audio = new Audio(path)
    console.log('loading audio...')
    return audio.addEventListener("canplaythrough",()=>{
        console.log('Audio loaded: '+path)
        return resolve(audio)
    });
});

export {loadImage,loadAudio}