/* Copyright (c) 2020, Jonas Lauener & Wingtra AG
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/. */

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

