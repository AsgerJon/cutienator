//  Written by hand on 2026-11-25 from
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumejob_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: the destructor (Qt declares none), 'hoveredPickers' (it
//  gives a QList) and 'dispatchPickEvents' (it takes a std::vector).
//  'PickBoundingVolumeJobPrivate' is named in full, as Qt declares it
//  in Qt3DRender::Render.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumejob_p.h>
#include <cstring>

//  A Qt3DRender::Render::PickBoundingVolumeJob that Python can take
//  functions over in. Every Qt3DRender::Render::PickBoundingVolumeJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Render_PickBoundingVolumeJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_PickBoundingVolumeJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_PickBoundingVolumeJobCall2)(const void *, int *);
class CuteQt3DRender_Render_PickBoundingVolumeJob : public Qt3DRender::Render::PickBoundingVolumeJob {
public:
  using Qt3DRender::Render::PickBoundingVolumeJob::PickBoundingVolumeJob;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render21PickBoundingVolumeJob9runHelperEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DRender::Render::PickBoundingVolumeJob::runHelper()
  bool runHelper() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_PickBoundingVolumeJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_PickBoundingVolumeJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Render::PickBoundingVolumeJob::runHelper();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_PickBoundingVolumeJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_PickBoundingVolumeJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_PickBoundingVolumeJobCall2 call = reinterpret_cast<CuteQt3DRender_Render_PickBoundingVolumeJobCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  Qt3DRender::Render::PickBoundingVolumeJob::PickBoundingVolumeJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickBoundingVolumeJob *ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJobC1Ev() {
  return new CuteQt3DRender_Render_PickBoundingVolumeJob();
}

//  void Qt3DRender::Render::PickBoundingVolumeJob::setRoot(Entity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob7setRootEPNS0_6EntityE(
    Qt3DRender::Render::PickBoundingVolumeJob *self,
    Qt3DRender::Render::Entity *root) {
  self->setRoot(root);
}

//  bool Qt3DRender::Render::PickBoundingVolumeJob::processMouseEvent(QObject
//      *object, QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob17processMouseEventEP7QObjectP11QMouseEvent(
    Qt3DRender::Render::PickBoundingVolumeJob *self,
    QObject *object,
    QMouseEvent *event) {
  return self->processMouseEvent(object, event);
}

//  void Qt3DRender::Render::PickBoundingVolumeJob::markPickersDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob16markPickersDirtyEv(
    Qt3DRender::Render::PickBoundingVolumeJob *self) {
  self->markPickersDirty();
}

//  bool Qt3DRender::Render::PickBoundingVolumeJob::pickersDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render21PickBoundingVolumeJob12pickersDirtyEv(
    const Qt3DRender::Render::PickBoundingVolumeJob *self) {
  return self->pickersDirty();
}

//  HObjectPicker
//      Qt3DRender::Render::PickBoundingVolumeJob::currentPicker() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::HObjectPicker *ritual_ZNK10Qt3DRender6Render21PickBoundingVolumeJob13currentPickerEv(
    const Qt3DRender::Render::PickBoundingVolumeJob *self) {
  return new Qt3DRender::Render::HObjectPicker(self->currentPicker());
}

//  void Qt3DRender::Render::PickBoundingVolumeJob::processPickEvent(const
//      PickingUtils::PickConfiguration &pickConfiguration, QObject *object,
//      const QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob16processPickEventERKNS0_12PickingUtils17PickConfigurationEP7QObjectPK11QMouseEvent(
    Qt3DRender::Render::PickBoundingVolumeJob *self,
    const Qt3DRender::Render::PickingUtils::PickConfiguration *pickConfiguration,
    QObject *object,
    const QMouseEvent *event) {
  self->processPickEvent(*pickConfiguration, object, event);
}

//  void
//      Qt3DRender::Render::PickBoundingVolumeJob::clearPreviouslyHoveredPickers()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob29clearPreviouslyHoveredPickersEv(
    Qt3DRender::Render::PickBoundingVolumeJob *self) {
  self->clearPreviouslyHoveredPickers();
}

//  Qt3DRender::Render::PickBoundingVolumeJobPrivate
//      *Qt3DRender::Render::PickBoundingVolumeJob::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickBoundingVolumeJobPrivate *ritual_ZN10Qt3DRender6Render21PickBoundingVolumeJob6d_funcEv(
    Qt3DRender::Render::PickBoundingVolumeJob *self) {
  return self->d_func();
}

//  const Qt3DRender::Render::PickBoundingVolumeJobPrivate
//      *Qt3DRender::Render::PickBoundingVolumeJob::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::PickBoundingVolumeJobPrivate *ritual_ZNK10Qt3DRender6Render21PickBoundingVolumeJob6d_funcEv(
    const Qt3DRender::Render::PickBoundingVolumeJob *self) {
  return self->d_func();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_PickBoundingVolumeJob, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_PickBoundingVolumeJob(
    Qt3DRender::Render::PickBoundingVolumeJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_PickBoundingVolumeJob *>(self)->take(key, call);
}

//  bool Qt3DRender::Render::PickBoundingVolumeJob::runHelper()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render21PickBoundingVolumeJob9runHelperEv(
    Qt3DRender::Render::PickBoundingVolumeJob *self) {
  return self->Qt3DRender::Render::PickBoundingVolumeJob::runHelper();
}
