dummy authentication plugin for Openstack clients
=================================================

This is a plugin for OpenStack Clients which provides a dummy auth system for
testing.

Test 
====


 keystone --os-auth-system dummy --dummy-arg "hello moto" token-get 
