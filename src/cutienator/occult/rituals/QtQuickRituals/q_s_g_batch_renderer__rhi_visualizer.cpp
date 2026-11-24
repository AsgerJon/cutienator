//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhivisualizer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhivisualizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGBatchRenderer::RhiVisualizer that Python can take functions over in. Every QSGBatchRenderer::RhiVisualizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall0)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall1)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall2)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall3)(const void *, QSGBatchRenderer::Node *, uint, int *);
class CuteQSGBatchRenderer_RhiVisualizer : public QSGBatchRenderer::RhiVisualizer {
public:
  using QSGBatchRenderer::RhiVisualizer::RhiVisualizer;
  CuteQSGBatchRenderer_RhiVisualizer(const QSGBatchRenderer::RhiVisualizer &other) : QSGBatchRenderer::RhiVisualizer(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer9visualizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEPNS_4NodeEj")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSGBatchRenderer::RhiVisualizer::prepareVisualize()
  void prepareVisualize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall0 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::prepareVisualize();
  }

  //  void QSGBatchRenderer::RhiVisualizer::visualize()
  void visualize() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall1 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::visualize();
  }

  //  void QSGBatchRenderer::RhiVisualizer::releaseResources()
  void releaseResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall2 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::releaseResources();
  }

  //  void QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n,
  //      uint parentChanges)
  void visualizeChangesPrepare(
      QSGBatchRenderer::Node *n,
      uint parentChanges) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall3 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall3>(taken[3]);
      call(this, n, parentChanges, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Visualizer::visualizeChangesPrepare(n, parentChanges);
  }
};

//  a Python function taken by a CuteQSGBatchRenderer_RhiVisualizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBatchRenderer_RhiVisualizer(
    QSGBatchRenderer::RhiVisualizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBatchRenderer_RhiVisualizer *>(self)->take(key, call);
}
