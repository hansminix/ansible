#!/bin/bash
/usr/sbin/squid -k parse 2>&1 >/dev/null | grep -E 'WARNING|ERROR|FATAL'