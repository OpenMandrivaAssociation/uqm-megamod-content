%define base_name	uqm-megamod

Name:		%{base_name}-content
Version:	0.8.0.85
Release:	2
Summary:	Mandatory content package for Ur-Quan Masters Megamod game
License:	GPL
Group:		Games/Strategy
URL:		https://megamod.serosis.net/Releases
Source:		http://files.serosis.net/MegaMod/%{version}/mm-%{version}-content.uqm
Source1:	http://files.serosis.net/MegaMod/%{version}/mm-%{version}-hd.uqm
Source2:	http://files.serosis.net/MegaMod/%{version}/mm-%{version}-3dovoice.uqm
Source3:	http://files.serosis.net/MegaMod/uqm-0.7.0-3DOMusicRemastered.uqm
Source4:	http://files.serosis.net/MegaMod/uqm-0.7.0-3dovideo.uqm
Source5:	http://files.serosis.net/MegaMod/%{version}/mm-%{version}-sol-textures.uqm
Source6:	http://files.serosis.net/MegaMod/%{version}/mm-%{version}-yellow-fried.uqm
Source7:	http://files.serosis.net/MegaMod/%{version}/mm-0.8.0.85-vols-remix.uqm
Source8:	http://files.serosis.net/MegaMod/%{version}/mm-0.8.0.85-vol-space.uqm
Source9:	http://files.serosis.net/MegaMod/%{version}/mm-0.8.0.85-rmx-utwig.uqm
Source10:	http://files.serosis.net/MegaMod/%{version}/mm-0.8.0.85-remix-timing.uqm
Source11:	http://files.serosis.net/MegaMod/uqm-remix-hqspace.uqm
Source12:	http://files.serosis.net/MegaMod/%{version}/mm-0.8.0.85-tarps-choice.uqm
# http://www.warpstormstudios.com/uqmmod/ -- Melnorme 1.3, Syreen 1.0
Source13:	http://www.warpstormstudios.com/uqmmod/MelnormeVoiceFixMMAddon.uqm
Source14:	http://www.warpstormstudios.com/uqmmod/SyreenVoiceFixMMAddon.uqm
# FIXME we may want to package those into a separate package
# (files conflict with the English language version):
#	http://files.serosis.net/Localization/Japanese/uqm-0.7.0-3dovideoJP.uqm
#	http://files.serosis.net/Localization/Japanese/uqm-0.7.0-3dovoiceJP.uqm
Requires:	%{base_name}
%rename %{base_name}-data
BuildArch:	noarch

%description
The Ur-Quan Masters is a port of the 3DO version of Star Control 2.

%prep
%setup -c -q

%build

%install
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/content/addons
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}/content

cat >%{buildroot}%{_gamesdatadir}/%{base_name}/content/version <<EOF
%{version}

$(date +"%%a %%b %%e %%H:%%M:%%S %%Y %%z")
EOF

cd %{buildroot}%{_gamesdatadir}/%{base_name}/content/addons
unzip %{S:1}
unzip %{S:2}
unzip %{S:3}
unzip %{S:4}
unzip %{S:5}
unzip %{S:6}
unzip %{S:7}
unzip %{S:8}
unzip %{S:9}
unzip %{S:10}
unzip -o %{S:11}
unzip %{S:12}
unzip %{S:13}
unzip %{S:14}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/content/*
