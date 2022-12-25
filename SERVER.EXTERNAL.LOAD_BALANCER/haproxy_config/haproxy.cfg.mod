defaults
  mode http
  log global
  option httplog
  option  http-server-close
  option  dontlognull
  option  redispatch
  option  contstats
  retries 3
  backlog 10000
  timeout client          25s
  timeout connect          5s
  timeout server          25s
# timeout tunnel available in ALOHA 5.5 or HAProxy 1.5-dev10 and higher
  timeout tunnel        3600s
  timeout http-keep-alive  1s
  timeout http-request    15s
  timeout queue           30s
  timeout tarpit          60s
  default-server inter 3s rise 2 fall 3
  option forwardfor

frontend ft_web
  bind *:80 name http
  maxconn 10000
  default_backend bk_web

backend bk_web                      
  balance roundrobin
  server websrv1 172.17.0.2:8080 maxconn 10000 weight 10 cookie websrv1 check
#  server websrv2 192.168.10.12:8080 maxconn 10000 weight 10 cookie websrv2 check
