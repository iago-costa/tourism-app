#!/usr/bin/env bash
set -euo pipefail

CF_API="https://api.cloudflare.com/client/v4"
DOMAIN="${DOMAIN:-vivdio.com}"
ORIGIN_IP="${ORIGIN_IP:-137.131.129.228}"

if [[ -z "${CF_API_TOKEN:-}" || -z "${CF_ZONE_ID:-}" ]]; then
  echo "CF_API_TOKEN e CF_ZONE_ID sao obrigatorios."
  exit 1
fi

record_id=$(curl -sS -X GET "${CF_API}/zones/${CF_ZONE_ID}/dns_records?name=tourism.${DOMAIN}&type=A" \
  -H "Authorization: Bearer ${CF_API_TOKEN}" -H "Content-Type: application/json" | jq -r '.result[0].id // empty')

payload=$(jq -n --arg name "tourism.${DOMAIN}" --arg ip "$ORIGIN_IP" \
  '{type:"A",name:$name,content:$ip,proxied:true,ttl:1,comment:"Tourism app"}')

if [[ -n "$record_id" ]]; then
  curl -sS -X PUT "${CF_API}/zones/${CF_ZONE_ID}/dns_records/${record_id}" \
    -H "Authorization: Bearer ${CF_API_TOKEN}" -H "Content-Type: application/json" -d "$payload" >/dev/null
else
  curl -sS -X POST "${CF_API}/zones/${CF_ZONE_ID}/dns_records" \
    -H "Authorization: Bearer ${CF_API_TOKEN}" -H "Content-Type: application/json" -d "$payload" >/dev/null
fi

echo "OK tourism.${DOMAIN} -> ${ORIGIN_IP}"
