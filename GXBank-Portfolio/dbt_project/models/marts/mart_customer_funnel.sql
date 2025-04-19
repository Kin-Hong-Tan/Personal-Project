SELECT channel, COUNT(*) as total_signups
FROM {{ ref('stg_customer_acquisition') }}
GROUP BY channel