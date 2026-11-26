//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractslider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(abstractslider)
#if QT_CONFIG(abstractslider)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(abstractslider)
#include <QtWidgets/qabstractslider.h>
#endif
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractslider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qabstractslider.h>
#include <QtGui/qevent.h>
#include <QtWidgets/private/qabstractslider_p.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <limits.h>
#include <QtWidgets/private/qapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractslider.cpp, line 179, as _ZN22QAbstractSliderPrivateC1Ev
inline QAbstractSliderPrivate::QAbstractSliderPrivate()
    : minimum(0), maximum(99), pageStep(10), value(0), position(0), pressValue(-1),
      singleStep(1), singleStepFromItemView(-1), viewMayChangeSingleStep(true), offset_accumulated(0), tracking(true),
      blocktracking(false), pressed(false),
      invertedAppearance(false), invertedControls(false),
      orientation(Qt::Horizontal), repeatAction(QAbstractSlider::SliderNoAction)
{
}

//  from src/widgets/widgets/qabstractslider.cpp, line 188, as _ZN22QAbstractSliderPrivateD1Ev
inline QAbstractSliderPrivate::~QAbstractSliderPrivate()
{
}

//  from src/widgets/widgets/qabstractslider.cpp, line 215, as _ZN22QAbstractSliderPrivate8setStepsEii
inline void QAbstractSliderPrivate::setSteps(int single, int page)
{
    Q_Q(QAbstractSlider);
    singleStep = qAbs(single);
    pageStep = qAbs(page);
    q->sliderChange(QAbstractSlider::SliderStepsChange);
}

//  from src/widgets/widgets/qabstractslider.cpp, line 816, as _ZN22QAbstractSliderPrivate24itemviewChangeSingleStepEi
inline void QAbstractSliderPrivate::itemviewChangeSingleStep(int step)
{
    singleStepFromItemView = step;
    if (viewMayChangeSingleStep && singleStep != step)
        setSteps(step, pageStep);
}

//  from src/widgets/widgets/qabstractslider.cpp, line 661, as _ZN22QAbstractSliderPrivate13scrollByDeltaEN2Qt11OrientationE6QFlagsINS0_16KeyboardModifierEEi
inline bool QAbstractSliderPrivate::scrollByDelta(Qt::Orientation orientation, Qt::KeyboardModifiers modifiers, int delta)
{
    Q_Q(QAbstractSlider);
    int stepsToScroll = 0;
    // in Qt scrolling to the right gives negative values.
    if (orientation == Qt::Horizontal)
        delta = -delta;
    qreal offset = qreal(delta) / 120;

    if ((modifiers & Qt::ControlModifier) || (modifiers & Qt::ShiftModifier)) {
        // Scroll one page regardless of delta:
        stepsToScroll = qBound(-pageStep, int(offset * pageStep), pageStep);
        offset_accumulated = 0;
    } else {
        // Calculate how many lines to scroll. Depending on what delta is (and
        // offset), we might end up with a fraction (e.g. scroll 1.3 lines). We can
        // only scroll whole lines, so we keep the reminder until next event.
        qreal stepsToScrollF =
#if QT_CONFIG(wheelevent)
                QApplication::wheelScrollLines() *
#endif
                offset * effectiveSingleStep();
        // Check if wheel changed direction since last event:
        if (offset_accumulated != 0 && (offset / offset_accumulated) < 0)
            offset_accumulated = 0;

        offset_accumulated += stepsToScrollF;

        // Don't scroll more than one page in any case:
        stepsToScroll = qBound(-pageStep, int(offset_accumulated), pageStep);

        offset_accumulated -= int(offset_accumulated);
        if (stepsToScroll == 0) {
            // We moved less than a line, but might still have accumulated partial scroll,
            // unless we already are at one of the ends.
            const float effective_offset = invertedControls ? -offset_accumulated : offset_accumulated;
            if (effective_offset > 0.f && value < maximum)
                return true;
            if (effective_offset < 0.f && value > minimum)
                return true;
            offset_accumulated = 0;
            return false;
        }
    }

    if (invertedControls)
        stepsToScroll = -stepsToScroll;

    int prevValue = value;
    position = bound(overflowSafeAdd(stepsToScroll)); // value will be updated by triggerAction()
    q->triggerAction(QAbstractSlider::SliderMove);

    if (prevValue == value) {
        offset_accumulated = 0;
        return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  A QAbstractSliderPrivate that Python can take functions over in. Every QAbstractSliderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(abstractslider)
typedef int (*CuteQAbstractSliderPrivateCall0)(const void *, int, int *);
#endif  // QT_CONFIG(abstractslider)
typedef void (*CuteQAbstractSliderPrivateCall1)(const void *, bool, int *);
typedef void (*CuteQAbstractSliderPrivateCall2)(const void *, int, int *);
typedef void (*CuteQAbstractSliderPrivateCall3)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall4)(const void *, int *);
typedef void * (*CuteQAbstractSliderPrivateCall5)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractSliderPrivateCall6)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractSliderPrivateCall7)(const void *, int *);
typedef int (*CuteQAbstractSliderPrivateCall8)(const void *, int *);
typedef const QImage * (*CuteQAbstractSliderPrivateCall9)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall10)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall11)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall12)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall13)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall14)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall15)(const void *, int *);
typedef void (*CuteQAbstractSliderPrivateCall16)(const void *, int *);
typedef bool (*CuteQAbstractSliderPrivateCall17)(const void *, int *);
typedef bool (*CuteQAbstractSliderPrivateCall18)(const void *, int *);
class CuteQAbstractSliderPrivate : public QAbstractSliderPrivate {
public:
  using QAbstractSliderPrivate::QAbstractSliderPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZNK22QAbstractSliderPrivate5boundEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractslider)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(abstractslider)
  //  int QAbstractSliderPrivate::bound(int val) const
  int bound(int val) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall0 call = reinterpret_cast<CuteQAbstractSliderPrivateCall0>(taken[0]);
      int given = call(this, val, &handled);
      if (handled) return given;
    }
    return QAbstractSliderPrivate::bound(val);
  }
#endif  // QT_CONFIG(abstractslider)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall1 call = reinterpret_cast<CuteQAbstractSliderPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall2 call = reinterpret_cast<CuteQAbstractSliderPrivateCall2>(taken[2]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall3 call = reinterpret_cast<CuteQAbstractSliderPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall4 call = reinterpret_cast<CuteQAbstractSliderPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall5 call = reinterpret_cast<CuteQAbstractSliderPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall6 call = reinterpret_cast<CuteQAbstractSliderPrivateCall6>(taken[6]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall7 call = reinterpret_cast<CuteQAbstractSliderPrivateCall7>(taken[7]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall8 call = reinterpret_cast<CuteQAbstractSliderPrivateCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall9 call = reinterpret_cast<CuteQAbstractSliderPrivateCall9>(taken[9]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall10 call = reinterpret_cast<CuteQAbstractSliderPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall11 call = reinterpret_cast<CuteQAbstractSliderPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall12 call = reinterpret_cast<CuteQAbstractSliderPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall13 call = reinterpret_cast<CuteQAbstractSliderPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall14 call = reinterpret_cast<CuteQAbstractSliderPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall15 call = reinterpret_cast<CuteQAbstractSliderPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall16 call = reinterpret_cast<CuteQAbstractSliderPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall17 call = reinterpret_cast<CuteQAbstractSliderPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractSliderPrivateCall18 call = reinterpret_cast<CuteQAbstractSliderPrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractSlider *QAbstractSliderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractSlider *ritual_ZN22QAbstractSliderPrivate6q_funcEv(
    QAbstractSliderPrivate *self) {
  return self->q_func();
}

//  const QAbstractSlider *QAbstractSliderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSlider *ritual_ZNK22QAbstractSliderPrivate6q_funcEv(
    const QAbstractSliderPrivate *self) {
  return self->q_func();
}

//  QAbstractSliderPrivate::QAbstractSliderPrivate()
extern "C" Q_DECL_EXPORT
QAbstractSliderPrivate *ritual_ZN22QAbstractSliderPrivateC1Ev() {
  return new CuteQAbstractSliderPrivate();
}

//  QAbstractSliderPrivate::~QAbstractSliderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSliderPrivateD1Ev(QAbstractSliderPrivate *self) {
  delete self;
}

//  void QAbstractSliderPrivate::setSteps(int single, int page)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSliderPrivate8setStepsEii(
    QAbstractSliderPrivate *self,
    int single,
    int page) {
  self->setSteps(single, page);
}

//  int QAbstractSliderPrivate::effectiveSingleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAbstractSliderPrivate19effectiveSingleStepEv(
    const QAbstractSliderPrivate *self) {
  return self->effectiveSingleStep();
}

//  void QAbstractSliderPrivate::itemviewChangeSingleStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSliderPrivate24itemviewChangeSingleStepEi(
    QAbstractSliderPrivate *self,
    int step) {
  self->itemviewChangeSingleStep(step);
}

//  int QAbstractSliderPrivate::bound(int val) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAbstractSliderPrivate5boundEi(
    const QAbstractSliderPrivate *self,
    int val) {
  return self->bound(val);
}

//  int QAbstractSliderPrivate::overflowSafeAdd(int add) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAbstractSliderPrivate15overflowSafeAddEi(
    const QAbstractSliderPrivate *self,
    int add) {
  return self->overflowSafeAdd(add);
}

//  void QAbstractSliderPrivate::setAdjustedSliderPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSliderPrivate25setAdjustedSliderPositionEi(
    QAbstractSliderPrivate *self,
    int position) {
  self->setAdjustedSliderPosition(position);
}

//  bool QAbstractSliderPrivate::scrollByDelta(Qt::Orientation orientation,
//      Qt::KeyboardModifiers modifiers, int delta)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSliderPrivate13scrollByDeltaEN2Qt11OrientationE6QFlagsINS0_16KeyboardModifierEEi(
    QAbstractSliderPrivate *self,
    Qt::Orientation orientation,
    int modifiers,
    int delta) {
  return self->scrollByDelta(
      orientation,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      delta);
}

//  a Python function taken by a CuteQAbstractSliderPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSliderPrivate(
    QAbstractSliderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSliderPrivate *>(self)->take(key, call);
}

//  int QAbstractSliderPrivate::bound(int val) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAbstractSliderPrivate5boundEi(
    const QAbstractSliderPrivate *self,
    int val) {
  return self->QAbstractSliderPrivate::bound(val);
}

#endif  // QT_CONFIG(abstractslider)
#endif  // QT_CONFIG(abstractslider)
