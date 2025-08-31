# properties/utils.py
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    try:
        # Connect to Redis (default cache alias)
        redis_conn = get_redis_connection("default")

        # Get Redis server INFO
        info = redis_conn.info()

        # Extract hits and misses
        keyspace_hits = info.get("keyspace_hits", 0)
        keyspace_misses = info.get("keyspace_misses", 0)

        # Avoid division by zero
        total = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total) if total > 0 else 0

        metrics = {
            "keyspace_hits": keyspace_hits,
            "keyspace_misses": keyspace_misses,
            "hit_ratio": round(hit_ratio, 2),
        }

        # Log metrics
        logger.info("Redis cache metrics: %s", metrics)

        return metrics

    except Exception as e:
        logger.error("Error retrieving Redis cache metrics: %s", str(e))
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0,
        }
