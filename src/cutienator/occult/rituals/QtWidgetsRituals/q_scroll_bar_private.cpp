//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qscrollbar_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qapplication.h>
#include <QtGui/qcursor.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qpointer.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#include <QtWidgets/private/qmenu_p.h>
#endif
#include <limits.h>
#include <QtWidgets/private/qscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qscrollbar.cpp, line 232, as _ZN17QScrollBarPrivate15activateControlEji
inline void QScrollBarPrivate::activateControl(uint control, int threshold)
{
    QAbstractSlider::SliderAction action = QAbstractSlider::SliderNoAction;
    switch (control) {
    case QStyle::SC_ScrollBarAddPage:
        action = QAbstractSlider::SliderPageStepAdd;
        break;
    case QStyle::SC_ScrollBarSubPage:
        action = QAbstractSlider::SliderPageStepSub;
        break;
    case QStyle::SC_ScrollBarAddLine:
        action = QAbstractSlider::SliderSingleStepAdd;
        break;
    case QStyle::SC_ScrollBarSubLine:
        action = QAbstractSlider::SliderSingleStepSub;
        break;
    case QStyle::SC_ScrollBarFirst:
        action = QAbstractSlider::SliderToMinimum;
        break;
    case QStyle::SC_ScrollBarLast:
        action = QAbstractSlider::SliderToMaximum;
        break;
    default:
        break;
    }

    if (action) {
        q_func()->setRepeatAction(action, threshold);
        q_func()->triggerAction(action);
    }
}

//  from src/widgets/widgets/qscrollbar.cpp, line 264, as _ZN17QScrollBarPrivate16stopRepeatActionEv
inline void QScrollBarPrivate::stopRepeatAction()
{
    Q_Q(QScrollBar);
    QStyle::SubControl tmp = pressedControl;
    q->setRepeatAction(QAbstractSlider::SliderNoAction);
    pressedControl = QStyle::SC_None;

    if (tmp == QStyle::SC_ScrollBarSlider)
        q->setSliderDown(false);

    QStyleOptionSlider opt;
    q->initStyleOption(&opt);
    q->repaint(q->style()->subControlRect(QStyle::CC_ScrollBar, &opt, tmp, q));
}

//  from src/widgets/widgets/qscrollbar.cpp, line 720, as _ZNK17QScrollBarPrivate20pixelPosToRangeValueEi
inline int QScrollBarPrivate::pixelPosToRangeValue(int pos) const
{
    Q_Q(const QScrollBar);
    QStyleOptionSlider opt;
    q->initStyleOption(&opt);
    QRect gr = q->style()->subControlRect(QStyle::CC_ScrollBar, &opt,
                                          QStyle::SC_ScrollBarGroove, q);
    QRect sr = q->style()->subControlRect(QStyle::CC_ScrollBar, &opt,
                                          QStyle::SC_ScrollBarSlider, q);
    int sliderMin, sliderMax, sliderLength;

    if (orientation == Qt::Horizontal) {
        sliderLength = sr.width();
        sliderMin = gr.x();
        sliderMax = gr.right() - sliderLength + 1;
        if (q->layoutDirection() == Qt::RightToLeft)
            opt.upsideDown = !opt.upsideDown;
    } else {
        sliderLength = sr.height();
        sliderMin = gr.y();
        sliderMax = gr.bottom() - sliderLength + 1;
    }

    return  QStyle::sliderValueFromPosition(minimum, maximum, pos - sliderMin,
                                            sliderMax - sliderMin, opt.upsideDown);
}

//  from src/widgets/widgets/qscrollbar.cpp, line 356, as _ZN17QScrollBarPrivate4initEv
inline void QScrollBarPrivate::init()
{
    Q_Q(QScrollBar);
    invertedControls = true;
    pressedControl = hoverControl = QStyle::SC_None;
    pointerOutsidePressedControl = false;
    QStyleOption opt;
    opt.initFrom(q);
    transient = q->style()->styleHint(QStyle::SH_ScrollBar_Transient, &opt, q);
    flashed = false;
    q->setFocusPolicy(Qt::NoFocus);
    QSizePolicy sp(QSizePolicy::Minimum, QSizePolicy::Fixed, QSizePolicy::Slider);
    if (orientation == Qt::Vertical)
        sp.transpose();
    q->setSizePolicy(sp);
    q->setAttribute(Qt::WA_WState_OwnSizePolicy, false);
    q->setAttribute(Qt::WA_OpaquePaintEvent);
}

//  from src/widgets/widgets/qscrollbar.cpp, line 172, as _ZN17QScrollBarPrivate18updateHoverControlERK6QPoint
inline bool QScrollBarPrivate::updateHoverControl(const QPoint &pos)
{
    Q_Q(QScrollBar);
    QRect lastHoverRect = hoverRect;
    QStyle::SubControl lastHoverControl = hoverControl;
    bool doesHover = q->testAttribute(Qt::WA_Hover);
    if (lastHoverControl != newHoverControl(pos) && doesHover) {
        q->update(lastHoverRect);
        q->update(hoverRect);
        return true;
    }
    return !doesHover;
}

//  from src/widgets/widgets/qscrollbar.cpp, line 186, as _ZN17QScrollBarPrivate15newHoverControlERK6QPoint
inline QStyle::SubControl QScrollBarPrivate::newHoverControl(const QPoint &pos)
{
    Q_Q(QScrollBar);
    QStyleOptionSlider opt;
    q->initStyleOption(&opt);
    opt.subControls = QStyle::SC_All;
    hoverControl = q->style()->hitTestComplexControl(QStyle::CC_ScrollBar, &opt, pos, q);
    if (hoverControl == QStyle::SC_None)
        hoverRect = QRect();
    else
        hoverRect = q->style()->subControlRect(QStyle::CC_ScrollBar, &opt, hoverControl, q);
    return hoverControl;
}

//  from src/widgets/widgets/qscrollbar.cpp, line 200, as _ZN17QScrollBarPrivate12setTransientEb
inline void QScrollBarPrivate::setTransient(bool value)
{
    Q_Q(QScrollBar);
    if (transient != value) {
        transient = value;
        if (q->isVisible()) {
            QStyleOptionSlider opt;
            q->initStyleOption(&opt);
            if (q->style()->styleHint(QStyle::SH_ScrollBar_Transient, &opt, q))
                q->update();
        } else if (!transient) {
            q->show();
        }
    }
}
//  -----------------------------------------------------------------------

//  A QScrollBarPrivate that Python can take functions over in. Every QScrollBarPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(abstractslider)
typedef int (*CuteQScrollBarPrivateCall0)(const void *, int, int *);
#endif  // QT_CONFIG(abstractslider)
typedef void (*CuteQScrollBarPrivateCall1)(const void *, bool, int *);
typedef void (*CuteQScrollBarPrivateCall2)(const void *, int, int *);
typedef void (*CuteQScrollBarPrivateCall3)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall4)(const void *, int *);
typedef void * (*CuteQScrollBarPrivateCall5)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQScrollBarPrivateCall6)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQScrollBarPrivateCall7)(const void *, int *);
typedef int (*CuteQScrollBarPrivateCall8)(const void *, int *);
typedef const QImage * (*CuteQScrollBarPrivateCall9)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall10)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall11)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall12)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall13)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall14)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall15)(const void *, int *);
typedef void (*CuteQScrollBarPrivateCall16)(const void *, int *);
typedef bool (*CuteQScrollBarPrivateCall17)(const void *, int *);
typedef bool (*CuteQScrollBarPrivateCall18)(const void *, int *);
class CuteQScrollBarPrivate : public QScrollBarPrivate {
public:
  using QScrollBarPrivate::QScrollBarPrivate;
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
      CuteQScrollBarPrivateCall0 call = reinterpret_cast<CuteQScrollBarPrivateCall0>(taken[0]);
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
      CuteQScrollBarPrivateCall1 call = reinterpret_cast<CuteQScrollBarPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScrollBarPrivateCall2 call = reinterpret_cast<CuteQScrollBarPrivateCall2>(taken[2]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQScrollBarPrivateCall3 call = reinterpret_cast<CuteQScrollBarPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQScrollBarPrivateCall4 call = reinterpret_cast<CuteQScrollBarPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[5]) {
      int handled = 0;
      CuteQScrollBarPrivateCall5 call = reinterpret_cast<CuteQScrollBarPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQScrollBarPrivateCall6 call = reinterpret_cast<CuteQScrollBarPrivateCall6>(taken[6]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQScrollBarPrivateCall7 call = reinterpret_cast<CuteQScrollBarPrivateCall7>(taken[7]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[8]) {
      int handled = 0;
      CuteQScrollBarPrivateCall8 call = reinterpret_cast<CuteQScrollBarPrivateCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[9]) {
      int handled = 0;
      CuteQScrollBarPrivateCall9 call = reinterpret_cast<CuteQScrollBarPrivateCall9>(taken[9]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQScrollBarPrivateCall10 call = reinterpret_cast<CuteQScrollBarPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQScrollBarPrivateCall11 call = reinterpret_cast<CuteQScrollBarPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQScrollBarPrivateCall12 call = reinterpret_cast<CuteQScrollBarPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[13]) {
      int handled = 0;
      CuteQScrollBarPrivateCall13 call = reinterpret_cast<CuteQScrollBarPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQScrollBarPrivateCall14 call = reinterpret_cast<CuteQScrollBarPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteQScrollBarPrivateCall15 call = reinterpret_cast<CuteQScrollBarPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[16]) {
      int handled = 0;
      CuteQScrollBarPrivateCall16 call = reinterpret_cast<CuteQScrollBarPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[17]) {
      int handled = 0;
      CuteQScrollBarPrivateCall17 call = reinterpret_cast<CuteQScrollBarPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQScrollBarPrivateCall18 call = reinterpret_cast<CuteQScrollBarPrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QScrollBar *QScrollBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZN17QScrollBarPrivate6q_funcEv(QScrollBarPrivate *self) {
  return self->q_func();
}

//  const QScrollBar *QScrollBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScrollBar *ritual_ZNK17QScrollBarPrivate6q_funcEv(
    const QScrollBarPrivate *self) {
  return self->q_func();
}

//  void QScrollBarPrivate::activateControl(uint control, int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScrollBarPrivate15activateControlEji(
    QScrollBarPrivate *self,
    uint control,
    int threshold) {
  self->activateControl(control, threshold);
}

//  void QScrollBarPrivate::stopRepeatAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScrollBarPrivate16stopRepeatActionEv(
    QScrollBarPrivate *self) {
  self->stopRepeatAction();
}

//  int QScrollBarPrivate::pixelPosToRangeValue(int pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QScrollBarPrivate20pixelPosToRangeValueEi(
    const QScrollBarPrivate *self,
    int pos) {
  return self->pixelPosToRangeValue(pos);
}

//  void QScrollBarPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScrollBarPrivate4initEv(QScrollBarPrivate *self) {
  self->init();
}

//  bool QScrollBarPrivate::updateHoverControl(const QPoint &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QScrollBarPrivate18updateHoverControlERK6QPoint(
    QScrollBarPrivate *self,
    const QPoint *pos) {
  return self->updateHoverControl(*pos);
}

//  QStyle::SubControl QScrollBarPrivate::newHoverControl(const QPoint &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZN17QScrollBarPrivate15newHoverControlERK6QPoint(
    QScrollBarPrivate *self,
    const QPoint *pos) {
  return self->newHoverControl(*pos);
}

//  void QScrollBarPrivate::setTransient(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScrollBarPrivate12setTransientEb(
    QScrollBarPrivate *self,
    bool value) {
  self->setTransient(value);
}

//  a Python function taken by a CuteQScrollBarPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollBarPrivate(
    QScrollBarPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScrollBarPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(scrollbar)
