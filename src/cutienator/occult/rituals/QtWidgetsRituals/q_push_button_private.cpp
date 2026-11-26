//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpushbutton_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qpushbutton_p.h>
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
#include <QtWidgets/private/qabstractbutton_p.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(buttongroup)
#include <QtWidgets/qbuttongroup.h>
#include <QtWidgets/private/qbuttongroup_p.h>
#endif
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qabstractbutton_p.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qpointer.h>
#include <algorithm>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#if QT_CONFIG(dialog)
#include <QtWidgets/private/qdialog_p.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpointer.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#endif
#include <QtCore/qdebug.h>
#include <QtWidgets/qlayoutitem.h>
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/qdialogbuttonbox.h>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#include <QtWidgets/private/qmenu_p.h>
#endif
#include <QtWidgets/private/qpushbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractbutton.cpp, line 31, as local:qabstractbutton.cpp:AUTO_REPEAT_DELAY
#define AUTO_REPEAT_DELAY  300

//  from src/widgets/widgets/qabstractbutton.cpp, line 32, as local:qabstractbutton.cpp:AUTO_REPEAT_INTERVAL
#define AUTO_REPEAT_INTERVAL 100

//  from src/widgets/widgets/qabstractbutton.cpp, line 139, as _ZN22QAbstractButtonPrivateC2EN11QSizePolicy11ControlTypeE
inline QAbstractButtonPrivate::QAbstractButtonPrivate(QSizePolicy::ControlType type)
    :
#ifndef QT_NO_SHORTCUT
    shortcutId(0),
#endif
    checkable(false), checked(false), autoRepeat(false), autoExclusive(false),
    down(false), blockRefresh(false), pressed(false),
#if QT_CONFIG(buttongroup)
    group(nullptr),
#endif
    autoRepeatDelay(AUTO_REPEAT_DELAY),
    autoRepeatInterval(AUTO_REPEAT_INTERVAL),
    controlType(type)
{}

//  from src/widgets/widgets/qpushbutton.cpp, line 643, as _ZNK18QPushButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE
inline QStyle::State QPushButtonPrivate::styleButtonState(QStyle::State state) const
{
    Q_Q(const QPushButton);
    state = QAbstractButtonPrivate::styleButtonState(state);
    if (menuOpen)
        state |= QStyle::State_Sunken;
    if (checked)
        state |= QStyle::State_On;
    if (!flat && !down)
        state |= QStyle::State_Raised;
    if (q->underMouse() && q->hasMouseTracking())
        state.setFlag(QStyle::State_MouseOver, hovering);
    return state;
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 434, as _ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE
inline QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State state) const
{
    if (down)
        state |= QStyle::State_Sunken;
    return state;
}

//  from src/widgets/widgets/qpushbutton.cpp, line 628, as _ZN18QPushButtonPrivate4initEv
inline void QPushButtonPrivate::init()
{
    Q_Q(QPushButton);
    q->setAttribute(Qt::WA_MacShowFocusRect);
    resetLayoutItemMargins();
}

//  from src/widgets/widgets/qpushbutton.cpp, line 587, as _ZN18QPushButtonPrivate20adjustedMenuPositionEv
#if QT_CONFIG(menu)
inline QPoint QPushButtonPrivate::adjustedMenuPosition()
{
    Q_Q(QPushButton);

    bool horizontal = true;
#if QT_CONFIG(toolbar)
    QToolBar *tb = qobject_cast<QToolBar*>(parent);
    if (tb && tb->orientation() == Qt::Vertical)
        horizontal = false;
#endif

    QWidgetItem item(q);
    QRect rect = item.geometry();
    rect.setRect(rect.x() - q->x(), rect.y() - q->y(), rect.width(), rect.height());

    QSize menuSize = menu->sizeHint();
    QPoint globalPos = q->mapToGlobal(rect.topLeft());
    int x = globalPos.x();
    int y = globalPos.y();
    const QRect availableGeometry = QWidgetPrivate::availableScreenGeometry(q, q->mapToGlobal(rect.center()));
    if (horizontal) {
        if (globalPos.y() + rect.height() + menuSize.height() <= availableGeometry.bottom()) {
            y += rect.height();
        } else if (globalPos.y() - menuSize.height() >= availableGeometry.y()) {
            y -= menuSize.height();
        }
        if (q->layoutDirection() == Qt::RightToLeft)
            x += rect.width() - menuSize.width();
    } else {
        if (globalPos.x() + rect.width() + menu->sizeHint().width() <= availableGeometry.right()) {
            x += rect.width();
        } else if (globalPos.x() - menuSize.width() >= availableGeometry.x()) {
            x -= menuSize.width();
        }
    }

    return QPoint(x,y);
}
#endif  // QT_CONFIG(menu)

//  from src/widgets/widgets/qpushbutton.cpp, line 635, as _ZN18QPushButtonPrivate22resetLayoutItemMarginsEv
inline void QPushButtonPrivate::resetLayoutItemMargins()
{
    Q_Q(QPushButton);
    QStyleOptionButton opt;
    q->initStyleOption(&opt);
    setLayoutItemMargins(QStyle::SE_PushButtonLayoutItem, &opt);
}

//  from src/widgets/widgets/qpushbutton.cpp, line 567, as _ZN18QPushButtonPrivate12popupPressedEv
#if QT_CONFIG(menu)
inline void QPushButtonPrivate::popupPressed()
{
    Q_Q(QPushButton);
    if (!down || !menu)
        return;

    menu->setNoReplayFor(q);

    QPoint menuPos = adjustedMenuPosition();

    QMenuPrivate::get(menu)->causedPopup.widget = q;

    //Because of a delay in menu effects, we must keep track of the
    //menu visibility to avoid flicker on button release
    menuOpen = true;
    QObject::connect(menu, &QMenu::aboutToHide,
                     q, [q, this]{ menuOpen = false; q->setDown(false); }, Qt::SingleShotConnection);
    menu->popup(menuPos);
}
#endif  // QT_CONFIG(menu)

//  from src/widgets/widgets/qpushbutton.cpp, line 257, as _ZNK18QPushButtonPrivate12dialogParentEv
#if QT_CONFIG(dialog)
inline QDialog *QPushButtonPrivate::dialogParent() const
{
    Q_Q(const QPushButton);
    const QWidget *p = q;
    while (p && !p->isWindow()) {
        p = p->parentWidget();
        if (const QDialog *dialog = qobject_cast<const QDialog *>(p))
            return const_cast<QDialog *>(dialog);
    }
    return nullptr;
}
#endif  // QT_CONFIG(dialog)
//  -----------------------------------------------------------------------

//  A QPushButtonPrivate that Python can take functions over in. Every QPushButtonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(pushbutton)
typedef int (*CuteQPushButtonPrivateCall0)(const void *, int, int *);
#endif  // QT_CONFIG(pushbutton)
typedef void (*CuteQPushButtonPrivateCall1)(const void *, bool, int *);
typedef void (*CuteQPushButtonPrivateCall2)(const void *, int, int *);
typedef void (*CuteQPushButtonPrivateCall3)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall4)(const void *, int *);
typedef void * (*CuteQPushButtonPrivateCall5)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQPushButtonPrivateCall6)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQPushButtonPrivateCall7)(const void *, int *);
typedef int (*CuteQPushButtonPrivateCall8)(const void *, int *);
typedef const QImage * (*CuteQPushButtonPrivateCall9)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall10)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall11)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall12)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall13)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall14)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall15)(const void *, int *);
typedef void (*CuteQPushButtonPrivateCall16)(const void *, int *);
typedef bool (*CuteQPushButtonPrivateCall17)(const void *, int *);
typedef bool (*CuteQPushButtonPrivateCall18)(const void *, int *);
class CuteQPushButtonPrivate : public QPushButtonPrivate {
public:
  using QPushButtonPrivate::QPushButtonPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
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

#if QT_CONFIG(pushbutton)
  //  QStyle::State QPushButtonPrivate::styleButtonState(QStyle::State
  //      state) const
  QStyle::State styleButtonState(QStyle::State state) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPushButtonPrivateCall0 call = reinterpret_cast<CuteQPushButtonPrivateCall0>(taken[0]);
      int given = call(this, static_cast<int>(state.toInt()), &handled);
      if (handled) return QFlags<QStyle::StateFlag>::fromInt(given);
    }
    return QPushButtonPrivate::styleButtonState(state);
  }
#endif  // QT_CONFIG(pushbutton)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPushButtonPrivateCall1 call = reinterpret_cast<CuteQPushButtonPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPushButtonPrivateCall2 call = reinterpret_cast<CuteQPushButtonPrivateCall2>(taken[2]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPushButtonPrivateCall3 call = reinterpret_cast<CuteQPushButtonPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPushButtonPrivateCall4 call = reinterpret_cast<CuteQPushButtonPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPushButtonPrivateCall5 call = reinterpret_cast<CuteQPushButtonPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPushButtonPrivateCall6 call = reinterpret_cast<CuteQPushButtonPrivateCall6>(taken[6]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPushButtonPrivateCall7 call = reinterpret_cast<CuteQPushButtonPrivateCall7>(taken[7]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPushButtonPrivateCall8 call = reinterpret_cast<CuteQPushButtonPrivateCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPushButtonPrivateCall9 call = reinterpret_cast<CuteQPushButtonPrivateCall9>(taken[9]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPushButtonPrivateCall10 call = reinterpret_cast<CuteQPushButtonPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPushButtonPrivateCall11 call = reinterpret_cast<CuteQPushButtonPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQPushButtonPrivateCall12 call = reinterpret_cast<CuteQPushButtonPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[13]) {
      int handled = 0;
      CuteQPushButtonPrivateCall13 call = reinterpret_cast<CuteQPushButtonPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQPushButtonPrivateCall14 call = reinterpret_cast<CuteQPushButtonPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteQPushButtonPrivateCall15 call = reinterpret_cast<CuteQPushButtonPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[16]) {
      int handled = 0;
      CuteQPushButtonPrivateCall16 call = reinterpret_cast<CuteQPushButtonPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPushButtonPrivateCall17 call = reinterpret_cast<CuteQPushButtonPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQPushButtonPrivateCall18 call = reinterpret_cast<CuteQPushButtonPrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QPushButton *QPushButtonPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN18QPushButtonPrivate6q_funcEv(
    QPushButtonPrivate *self) {
  return self->q_func();
}

//  const QPushButton *QPushButtonPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPushButton *ritual_ZNK18QPushButtonPrivate6q_funcEv(
    const QPushButtonPrivate *self) {
  return self->q_func();
}

//  QPushButtonPrivate::QPushButtonPrivate()
extern "C" Q_DECL_EXPORT
QPushButtonPrivate *ritual_ZN18QPushButtonPrivateC1Ev() {
  return new CuteQPushButtonPrivate();
}

//  void QPushButtonPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPushButtonPrivate4initEv(QPushButtonPrivate *self) {
  self->init();
}

//  QPushButtonPrivate *QPushButtonPrivate::get(QPushButton *b)
extern "C" Q_DECL_EXPORT
QPushButtonPrivate *ritual_ZN18QPushButtonPrivate3getEP11QPushButton(
    QPushButton *b) {
  return QPushButtonPrivate::get(b);
}

#if QT_CONFIG(menu)
//  QPoint QPushButtonPrivate::adjustedMenuPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN18QPushButtonPrivate20adjustedMenuPositionEv(
    QPushButtonPrivate *self) {
  return new QPoint(self->adjustedMenuPosition());
}
#endif  // QT_CONFIG(menu)

//  void QPushButtonPrivate::resetLayoutItemMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPushButtonPrivate22resetLayoutItemMarginsEv(
    QPushButtonPrivate *self) {
  self->resetLayoutItemMargins();
}

#if QT_CONFIG(menu)
//  void QPushButtonPrivate::popupPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPushButtonPrivate12popupPressedEv(
    QPushButtonPrivate *self) {
  self->popupPressed();
}
#endif  // QT_CONFIG(menu)

//  QStyle::State QPushButtonPrivate::styleButtonState(QStyle::State state)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QPushButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE(
    const QPushButtonPrivate *self,
    int state) {
  return static_cast<int>(
      self->styleButtonState(
          QFlags<QStyle::StateFlag>::fromInt(state)).toInt());
}

#if QT_CONFIG(dialog)
//  QDialog *QPushButtonPrivate::dialogParent() const
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZNK18QPushButtonPrivate12dialogParentEv(
    const QPushButtonPrivate *self) {
  return self->dialogParent();
}
#endif  // QT_CONFIG(dialog)

//  a Python function taken by a CuteQPushButtonPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPushButtonPrivate(
    QPushButtonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPushButtonPrivate *>(self)->take(key, call);
}

//  QStyle::State QPushButtonPrivate::styleButtonState(QStyle::State state)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QPushButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE(
    const QPushButtonPrivate *self,
    int state) {
  return static_cast<int>(
      self->QPushButtonPrivate::styleButtonState(
          QFlags<QStyle::StateFlag>::fromInt(state)).toInt());
}

#endif  // QT_CONFIG(pushbutton)
#endif  // QT_CONFIG(pushbutton)
