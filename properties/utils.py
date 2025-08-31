# properties/utils.py
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        keyspace_hits = info.get("keyspace_hits", 0)
        keyspace_misses = info.get("keyspace_misses", 0)

        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": keyspace_hits,
            "keyspace_misses": keyspace_misses,
            "hit_ratio": round(hit_ratio, 2),
        }

        logger.info("Redis cache metrics: %s", metrics)
        return metrics

    except Exception as e:
        logger.error("Error retrieving Redis cache metrics: %s", str(e))
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0,
        }
