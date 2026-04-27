def get_recommendation(cluster):

    strategies = {
        0: "Provide premium products and exclusive offers.",
        1: "Focus on loyalty programs and early access.",
        2: "Use discount campaigns and engagement offers.",
        3: "Cross-selling and upselling opportunities.",
        4: "Retarget low-spending customers with offers."
    }

    return strategies.get(cluster, "General marketing strategy.")