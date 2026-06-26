-- Remove old tables if they exist
DROP TABLE IF EXISTS security_events;
DROP TABLE IF EXISTS security_alerts;
DROP TABLE IF EXISTS security_incidents;

---------------------------------------------------
-- SECURITY EVENTS
---------------------------------------------------

CREATE TABLE security_events
(
    event_id UUID,

    timestamp DateTime,

    source String,

    host String,

    username String,

    source_ip String,

    destination_ip String,

    event_type String,

    severity String,

    mitre_tactic String,

    mitre_technique String,

    message String,

    raw_log String
)

ENGINE = MergeTree

ORDER BY (timestamp, source, host);

---------------------------------------------------
-- SECURITY ALERTS
---------------------------------------------------

CREATE TABLE security_alerts
(
    alert_id UUID,

    event_id UUID,

    timestamp DateTime,

    rule_name String,

    severity String,

    mitre_tactic String,

    mitre_technique String,

    status String,

    description String
)

ENGINE = MergeTree

ORDER BY (timestamp, severity);

---------------------------------------------------
-- SECURITY INCIDENTS
---------------------------------------------------

CREATE TABLE security_incidents
(
    incident_id UUID,

    created_at DateTime,

    severity String,

    title String,

    status String,

    ai_summary String,

    remediation String
)

ENGINE = MergeTree

ORDER BY created_at;