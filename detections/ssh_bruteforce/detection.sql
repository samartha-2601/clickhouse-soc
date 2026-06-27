SELECT
    source_ip,
    any(username) AS username,
    any(host) AS host,
    COUNT(*) AS failures
FROM security_events
WHERE event_type = 'failed_login'
GROUP BY source_ip
HAVING failures >= 5;