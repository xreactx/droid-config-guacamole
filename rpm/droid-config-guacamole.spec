# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device guacamole
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty OnePlus 7 Pro

%define community_adaptation 1
%define pixel_ratio 2.25

#Device-specific usb-moded configuration
Provides: usb-moded-configs
Obsoletes: usb-moded-defaults

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

