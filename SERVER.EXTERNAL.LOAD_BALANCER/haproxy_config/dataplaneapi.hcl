config_version = 2

name = "a5b63adf83f5"

mode = "single"

dataplaneapi {
  host = "0.0.0.0"
  port = 5555

  user "admin" {
    insecure = true
    password = "admin@pass"
  }

  transaction {
    transaction_dir = "/tmp/haproxy"
  }

  advertised {}
}

haproxy {
  config_file = "/usr/local/etc/haproxy/haproxy.cfg"
  haproxy_bin = "/usr/sbin/haproxy"

  reload {
    reload_delay    = 5
    reload_cmd      = "service haproxy reload"
    restart_cmd     = "service haproxy restart"
    reload_strategy = "custom"
  }
}
