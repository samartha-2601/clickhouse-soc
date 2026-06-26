SELECT
    source_ip,
    COUNT(*) AS failures
FROM security_events
WHERE event_type='failed_login'
GROUP BY source_ip
HAVING failures >= 5;