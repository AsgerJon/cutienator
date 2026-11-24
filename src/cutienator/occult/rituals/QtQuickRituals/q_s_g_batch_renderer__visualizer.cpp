//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGBatchRenderer::Visualizer that Python can take functions over in. Every QSGBatchRenderer::Visualizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBatchRenderer_VisualizerCall0)(const void *, QSGBatchRenderer::Node *, uint, int *);
typedef void (*CuteQSGBatchRenderer_VisualizerCall1)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_VisualizerCall2)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_VisualizerCall3)(const void *, int *);
class CuteQSGBatchRenderer_Visualizer : public QSGBatchRenderer::Visualizer {
public:
  using QSGBatchRenderer::Visualizer::Visualizer;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEPNS_4NodeEj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer9visualizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n,
  //      uint parentChanges)
  void visualizeChangesPrepare(
      QSGBatchRenderer::Node *n,
      uint parentChanges) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBatchRenderer_VisualizerCall0 call = reinterpret_cast<CuteQSGBatchRenderer_VisualizerCall0>(taken[0]);
      call(this, n, parentChanges, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Visualizer::visualizeChangesPrepare(n, parentChanges);
  }

  //  void QSGBatchRenderer::Visualizer::prepareVisualize()
  void prepareVisualize() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBatchRenderer_VisualizerCall1 call = reinterpret_cast<CuteQSGBatchRenderer_VisualizerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGBatchRenderer::Visualizer::visualize()
  void visualize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBatchRenderer_VisualizerCall2 call = reinterpret_cast<CuteQSGBatchRenderer_VisualizerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGBatchRenderer::Visualizer::releaseResources()
  void releaseResources() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBatchRenderer_VisualizerCall3 call = reinterpret_cast<CuteQSGBatchRenderer_VisualizerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QSGBatchRenderer::Visualizer::~Visualizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10VisualizerD1Ev(
    QSGBatchRenderer::Visualizer *self) {
  delete self;
}

//  VisualizeMode QSGBatchRenderer::Visualizer::mode() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Visualizer::VisualizeMode ritual_ZNK16QSGBatchRenderer10Visualizer4modeEv(
    const QSGBatchRenderer::Visualizer *self) {
  return self->mode();
}

//  void QSGBatchRenderer::Visualizer::setMode(VisualizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10Visualizer7setModeENS0_13VisualizeModeE(
    QSGBatchRenderer::Visualizer *self,
    QSGBatchRenderer::Visualizer::VisualizeMode mode) {
  self->setMode(mode);
}

//  void QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n, uint
//      parentChanges)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEPNS_4NodeEj(
    QSGBatchRenderer::Visualizer *self,
    QSGBatchRenderer::Node *n,
    uint parentChanges) {
  self->visualizeChangesPrepare(n, parentChanges);
}

//  void QSGBatchRenderer::Visualizer::prepareVisualize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv(
    QSGBatchRenderer::Visualizer *self) {
  self->prepareVisualize();
}

//  void QSGBatchRenderer::Visualizer::visualize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10Visualizer9visualizeEv(
    QSGBatchRenderer::Visualizer *self) {
  self->visualize();
}

//  void QSGBatchRenderer::Visualizer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv(
    QSGBatchRenderer::Visualizer *self) {
  self->releaseResources();
}

//  a Python function taken by a CuteQSGBatchRenderer_Visualizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBatchRenderer_Visualizer(
    QSGBatchRenderer::Visualizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBatchRenderer_Visualizer *>(self)->take(key, call);
}
