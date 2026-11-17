"""
Interpretability tools for CNN fitness classifiers.

This package provides tools for computing and visualizing feature attributions
for the CNN nanobody stability classifier.

Methods supported:
1. DeepLIFT (using Captum library) with shuffle or frequency baselines
2. Sufficient Input Subsets (SIS) - finds minimal feature subsets that drive predictions

Modules:
    shared: Common utilities (CaptumCNNWrapper, sequence encoding)
    deeplift: DeepLIFT attribution computation and analysis
    sis: Core SIS algorithm (from Google Research)
    sis_analysis: SIS application to our models
    visualization: Plotting functions for interpretability results
"""

# Shared utilities
# DeepLIFT
from nabstab.interpretability.deeplift import (
    aggregate_to_position_importance,
    aggregate_to_position_signed,
    analyze_sequence,
    batch_analyze,
    compute_background_frequencies,
    compute_deeplift_attributions,
    create_frequency_baseline,
    create_shuffled_baselines,
)
from nabstab.interpretability.shared import (
    CaptumCNNWrapper,
    preprocess_sequence,
    sequence_to_onehot,
    string_to_tensor,
)

# SIS analysis
from nabstab.interpretability.sis_analysis import (
    create_sis_wrapper,
    run_sis_batch,
    run_sis_batch_with_sets,
    run_sis_single,
    sis_to_position_counts,
    verify_masked_baseline,
)

# SIS clustering
from nabstab.interpretability.sis_clustering import (
    cluster_dbscan,
    compute_distance_matrix,
    exact_match_cluster,
    extract_all_motifs,
    get_cluster_representative,
    jaccard_distance,
    sis_set_to_signature,
    summarize_clustering,
)

# Visualization
from nabstab.interpretability.visualization import (
    # SIS visualization
    AA_COLORS,
    plot_comparison_heatmaps,
    plot_deeplift_heatmap,
    plot_motif_heatmap,
    plot_position_importance,
    plot_sis_logo,
    plot_sis_position_frequency,
    plot_top_motifs,
    sis_sets_to_frequency_matrix,
)

__all__ = [
    # SIS visualization
    'AA_COLORS',
    # Shared
    'CaptumCNNWrapper',
    'aggregate_to_position_importance',
    'aggregate_to_position_signed',
    'analyze_sequence',
    'batch_analyze',
    'cluster_dbscan',
    # DeepLIFT
    'compute_background_frequencies',
    'compute_deeplift_attributions',
    'compute_distance_matrix',
    'create_frequency_baseline',
    'create_shuffled_baselines',
    # SIS analysis
    'create_sis_wrapper',
    'exact_match_cluster',
    'extract_all_motifs',
    'get_cluster_representative',
    'jaccard_distance',
    'plot_comparison_heatmaps',
    # Visualization
    'plot_deeplift_heatmap',
    'plot_motif_heatmap',
    'plot_position_importance',
    'plot_sis_logo',
    'plot_sis_position_frequency',
    'plot_top_motifs',
    'preprocess_sequence',
    'run_sis_batch',
    'run_sis_batch_with_sets',
    'run_sis_single',
    'sequence_to_onehot',
    # SIS clustering
    'sis_set_to_signature',
    'sis_sets_to_frequency_matrix',
    'sis_to_position_counts',
    'string_to_tensor',
    'summarize_clustering',
    'verify_masked_baseline',
]
