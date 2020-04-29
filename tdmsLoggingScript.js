const timestamp = new Date();
const timestampString =   
  timestamp.getUTCFullYear() + "-" + 
  timestamp.getUTCMonth() + "-" + 
  timestamp.getUTCDate() + "T" + 
  timestamp.getUTCHours() + "_" + 
  timestamp.getUTCMinutes() + "_" +
  timestamp.getUTCSeconds() + "." +
  timestamp.getUTCMilliseconds();

Scope.Export("~/Desktop/scope/tdms/acq_" + Index + "_" + timestampString + ".tdms")

Index++

