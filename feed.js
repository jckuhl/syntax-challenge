const axios = require('axios');

const url = 'https://feed.syntax.fm/rss';

const fetch = url => {
    return new Promise(async (resolve, reject)=> {
        try {
            const response = await axios({
                url,
                headers: {
                    'Content-Type': 'application/xml'
                }
            });
            resolve(response.data);
        } catch(error) {
            reject(error);
        }
    });
}

const findDuration = async (url)=> {
    const rss = await fetch(url);
    const timestamps = rss.match(/(<itunes:duration>)([0-9:]+)(<\/itunes:duration>)/g);
    console.log(timestamps.length);
    const totals = timestamps.map(stamp => {
        stamp = stamp.match(/(([0-9]{2}:[0-9]{2}:[0-9]{2})|([0-9]{2}:[0-9]{2}))/)[0];
        stamp = stamp.split(':');
        let hours, minutes, seconds;
        if(stamp.length === 2) {
            hours = 0;
            minutes = stamp[0];
            seconds = stamp[1];
        } else {
            hours = stamp[0];
            minutes = stamp[1];
            seconds = stamp[2];
        }
        return {
            hours: parseInt(hours),
            minutes: parseInt(minutes),
            seconds: parseInt(seconds)
        }
    }).reduce((accum, current)=> {
        accum.seconds += current.seconds;
        accum.minutes += current.minutes;
        accum.hours += current.hours;
        return accum;
    }, { seconds: 0, minutes: 0, hours: 0});
    
    let seconds = totals.seconds % 60;
    let minutes = Math.floor(totals.seconds / 60) + totals.minutes;
    let hours = Math.floor(minutes / 60) + totals.hours;
    minutes = minutes % 60;



    return {
        hours,
        minutes,
        seconds
    }

}

findDuration(url)
    .then(duration => console.log(`Duration: ${duration.hours}:${duration.minutes}:${duration.seconds}`));