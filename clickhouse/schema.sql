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

DROP TABLE IF EXISTS security_alerts;

CREATE TABLE security_alerts
(
    alert_id UUID,

    event_id UUID,

    created_at DateTime,

    updated_at DateTime,

    first_seen DateTime,

    last_seen DateTime,

    rule_id String,

    rule_name String,

    severity String,

    status String,

    source_ip String,

    host String,

    username String,

    event_count UInt32,

    mitre_tactic String,

    mitre_technique String,

    description String
)

ENGINE = MergeTree

ORDER BY (created_at, severity);

---------------------------------------------------
-- SECURITY INCIDENTS
---------------------------------------------------

DROP TABLE IF EXISTS security_incidents;

CREATE TABLE security_incidents
(
    incident_id UUID,

    created_at DateTime,

    updated_at DateTime,

    title String,

    severity String,

    status String,

    affected_host String,

    affected_user String,

    alert_count UInt32,

    mitre_tactics String,

    timeline String,

    ai_summary String
)
ENGINE = MergeTree
ORDER BY (created_at);



CREATE TABLE IF NOT EXISTS security_investigations
(
    investigation_id UUID,

    incident_id UUID,

    created_at DateTime,

    model String,

    investigation_json String,

    confidence Float32
)
ENGINE = MergeTree()
ORDER BY (created_at);