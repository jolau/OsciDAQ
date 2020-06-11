function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

const timestamp = new Date();
const timestampString =   
  timestamp.getUTCFullYear() + "-" + 
  pad(timestamp.getUTCMonth(), 2) + "-" + 
  pad(timestamp.getUTCDate(), 2) + "T" + 
  pad(timestamp.getUTCHours(), 2) + "_" + 
  pad(timestamp.getUTCMinutes(), 2) + "_" +
  pad(timestamp.getUTCSeconds(), 2) + "." +
  timestamp.getUTCMilliseconds();

if((Index - 1) % 1000 == 0) {
    var batchCounter = Math.floor((Index - 1) / 1000)
    BatchFolder = "batch_" + pad(batchCounter, 2) + "_" + timestampString + "/";
} else if(typeof BatchFolder == 'undefined') {
    BatchFolder = "";
}

Scope.Export("~/Documents/scope/" + BatchFolder + "acq_" + pad(Index, 7) + "_" + timestampString + ".tdms")

Index++
