//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractbutton_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qabstractbutton.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractbutton.cpp, line 31, as local:qabstractbutton.cpp:AUTO_REPEAT_DELAY
#define AUTO_REPEAT_DELAY  300

//  from src/widgets/widgets/qabstractbutton.cpp, line 32, as local:qabstractbutton.cpp:AUTO_REPEAT_INTERVAL
#define AUTO_REPEAT_INTERVAL 100

//  from src/widgets/widgets/qabstractbutton.cpp, line 434, as _ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE
inline QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State state) const
{
    if (down)
        state |= QStyle::State_Sunken;
    return state;
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 139, as _ZN22QAbstractButtonPrivateC1EN11QSizePolicy11ControlTypeE
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

//  from src/widgets/widgets/qabstractbutton.cpp, line 323, as _ZN22QAbstractButtonPrivate4initEv
inline void QAbstractButtonPrivate::init()
{
    Q_Q(QAbstractButton);

    // Query focus policy. Don't pass the QWidget pointer since QStyleSheetStyle will
    // (if in use) cache it derive incorrect style metrics from it.
    q->setFocusPolicy(Qt::FocusPolicy(q->style()->styleHint(QStyle::SH_Button_FocusPolicy,
                                                            nullptr, nullptr)));
    q->setSizePolicy(QSizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed, controlType));
    q->setAttribute(Qt::WA_WState_OwnSizePolicy, false);
    q->setForegroundRole(QPalette::ButtonText);
    q->setBackgroundRole(QPalette::Button);
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 346, as _ZN22QAbstractButtonPrivate5clickEv
inline void QAbstractButtonPrivate::click()
{
    Q_Q(QAbstractButton);

    down = false;
    blockRefresh = true;
    bool changeState = true;
    if (checked && queryCheckedButton() == q) {
        // the checked button of an exclusive or autoexclusive group cannot be unchecked
#if QT_CONFIG(buttongroup)
        if (group ? group->d_func()->exclusive : autoExclusive)
#else
        if (autoExclusive)
#endif
            changeState = false;
    }

    QPointer<QAbstractButton> guard(q);
    if (changeState) {
        q->nextCheckState();
        if (!guard)
            return;
    }
    blockRefresh = false;
    refresh();
    q->repaint();
    if (guard)
        emitReleased();
    if (guard)
        emitClicked();
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 337, as _ZN22QAbstractButtonPrivate7refreshEv
inline void QAbstractButtonPrivate::refresh()
{
    Q_Q(QAbstractButton);

    if (blockRefresh)
        return;
    q->update();
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 154, as _ZNK22QAbstractButtonPrivate15queryButtonListEv
inline QList<QAbstractButton *>QAbstractButtonPrivate::queryButtonList() const
{
#if QT_CONFIG(buttongroup)
    if (group)
        return group->d_func()->buttonList;
#endif

    if (!parent)
        return {};
    QList<QAbstractButton *> candidates = parent->findChildren<QAbstractButton *>();
    if (autoExclusive) {
        auto isNoMemberOfMyAutoExclusiveGroup = [](QAbstractButton *candidate) {
            return !candidate->autoExclusive()
#if QT_CONFIG(buttongroup)
                || candidate->group()
#endif
                ;
        };
        candidates.removeIf(isNoMemberOfMyAutoExclusiveGroup);
    }
    return candidates;
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 177, as _ZNK22QAbstractButtonPrivate18queryCheckedButtonEv
inline QAbstractButton *QAbstractButtonPrivate::queryCheckedButton() const
{
#if QT_CONFIG(buttongroup)
    if (group)
        return group->d_func()->checkedButton;
#endif

    Q_Q(const QAbstractButton);
    QList<QAbstractButton *> buttonList = queryButtonList();
    if (!autoExclusive || buttonList.size() == 1) // no group
        return nullptr;

    for (int i = 0; i < buttonList.size(); ++i) {
        QAbstractButton *b = buttonList.at(i);
        if (b->d_func()->checked && b != q)
            return b;
    }
    return checked  ? const_cast<QAbstractButton *>(q) : nullptr;
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 197, as _ZN22QAbstractButtonPrivate13notifyCheckedEv
inline void QAbstractButtonPrivate::notifyChecked()
{
#if QT_CONFIG(buttongroup)
    Q_Q(QAbstractButton);
    if (group) {
        QAbstractButton *previous = group->d_func()->checkedButton;
        group->d_func()->checkedButton = q;
        if (group->d_func()->exclusive && previous && previous != q)
            previous->nextCheckState();
    } else
#endif
    if (autoExclusive) {
        if (QAbstractButton *b = queryCheckedButton())
            b->setChecked(false);
    }
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 302, as _ZN22QAbstractButtonPrivate14fixFocusPolicyEv
inline void QAbstractButtonPrivate::fixFocusPolicy()
{
    Q_Q(QAbstractButton);
#if QT_CONFIG(buttongroup)
    if (!group && !autoExclusive)
#else
    if (!autoExclusive)
#endif
        return;

    QList<QAbstractButton *> buttonList = queryButtonList();
    for (int i = 0; i < buttonList.size(); ++i) {
        QAbstractButton *b = buttonList.at(i);
        if (!b->isCheckable())
            continue;
        b->setFocusPolicy((Qt::FocusPolicy) ((b == q || !q->isCheckable())
                                         ? (b->focusPolicy() | Qt::TabFocus)
                                         :  (b->focusPolicy() & ~Qt::TabFocus)));
    }
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 392, as _ZN22QAbstractButtonPrivate11emitPressedEv
inline void QAbstractButtonPrivate::emitPressed()
{
    Q_Q(QAbstractButton);
    QPointer<QAbstractButton> guard(q);
    emit q->pressed();
#if QT_CONFIG(buttongroup)
    if (guard && group) {
        emit group->idPressed(group->id(q));
        if (guard && group)
            emit group->buttonPressed(q);
    }
#endif
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 406, as _ZN22QAbstractButtonPrivate12emitReleasedEv
inline void QAbstractButtonPrivate::emitReleased()
{
    Q_Q(QAbstractButton);
    QPointer<QAbstractButton> guard(q);
    emit q->released();
#if QT_CONFIG(buttongroup)
    if (guard && group) {
        emit group->idReleased(group->id(q));
        if (guard && group)
            emit group->buttonReleased(q);
    }
#endif
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 378, as _ZN22QAbstractButtonPrivate11emitClickedEv
inline void QAbstractButtonPrivate::emitClicked()
{
    Q_Q(QAbstractButton);
    QPointer<QAbstractButton> guard(q);
    emit q->clicked(checked);
#if QT_CONFIG(buttongroup)
    if (guard && group) {
        emit group->idClicked(group->id(q));
        if (guard && group)
            emit group->buttonClicked(q);
    }
#endif
}

//  from src/widgets/widgets/qabstractbutton.cpp, line 420, as _ZN22QAbstractButtonPrivate11emitToggledEb
inline void QAbstractButtonPrivate::emitToggled(bool checked)
{
    Q_Q(QAbstractButton);
    QPointer<QAbstractButton> guard(q);
    emit q->toggled(checked);
#if QT_CONFIG(buttongroup)
    if (guard && group) {
        emit group->idToggled(group->id(q), checked);
        if (guard && group)
            emit group->buttonToggled(q, checked);
    }
#endif
}
//  -----------------------------------------------------------------------

//  A QAbstractButtonPrivate that Python can take functions over in. Every QAbstractButtonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractButtonPrivateCall0)(const void *, int, int *);
typedef void (*CuteQAbstractButtonPrivateCall1)(const void *, bool, int *);
typedef void (*CuteQAbstractButtonPrivateCall2)(const void *, int, int *);
typedef void (*CuteQAbstractButtonPrivateCall3)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall4)(const void *, int *);
typedef void * (*CuteQAbstractButtonPrivateCall5)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractButtonPrivateCall6)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractButtonPrivateCall7)(const void *, int *);
typedef int (*CuteQAbstractButtonPrivateCall8)(const void *, int *);
typedef const QImage * (*CuteQAbstractButtonPrivateCall9)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall10)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall11)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall12)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall13)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall14)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall15)(const void *, int *);
typedef void (*CuteQAbstractButtonPrivateCall16)(const void *, int *);
typedef bool (*CuteQAbstractButtonPrivateCall17)(const void *, int *);
typedef bool (*CuteQAbstractButtonPrivateCall18)(const void *, int *);
class CuteQAbstractButtonPrivate : public QAbstractButtonPrivate {
public:
  using QAbstractButtonPrivate::QAbstractButtonPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE")) {
      taken[0] = call;
      return true;
    }
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

  //  QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State
  //      state) const
  QStyle::State styleButtonState(QStyle::State state) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall0 call = reinterpret_cast<CuteQAbstractButtonPrivateCall0>(taken[0]);
      int given = call(this, static_cast<int>(state.toInt()), &handled);
      if (handled) return QFlags<QStyle::StateFlag>::fromInt(given);
    }
    return QAbstractButtonPrivate::styleButtonState(state);
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall1 call = reinterpret_cast<CuteQAbstractButtonPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall2 call = reinterpret_cast<CuteQAbstractButtonPrivateCall2>(taken[2]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall3 call = reinterpret_cast<CuteQAbstractButtonPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall4 call = reinterpret_cast<CuteQAbstractButtonPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall5 call = reinterpret_cast<CuteQAbstractButtonPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall6 call = reinterpret_cast<CuteQAbstractButtonPrivateCall6>(taken[6]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall7 call = reinterpret_cast<CuteQAbstractButtonPrivateCall7>(taken[7]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall8 call = reinterpret_cast<CuteQAbstractButtonPrivateCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall9 call = reinterpret_cast<CuteQAbstractButtonPrivateCall9>(taken[9]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall10 call = reinterpret_cast<CuteQAbstractButtonPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall11 call = reinterpret_cast<CuteQAbstractButtonPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall12 call = reinterpret_cast<CuteQAbstractButtonPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall13 call = reinterpret_cast<CuteQAbstractButtonPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall14 call = reinterpret_cast<CuteQAbstractButtonPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall15 call = reinterpret_cast<CuteQAbstractButtonPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall16 call = reinterpret_cast<CuteQAbstractButtonPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall17 call = reinterpret_cast<CuteQAbstractButtonPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractButtonPrivateCall18 call = reinterpret_cast<CuteQAbstractButtonPrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractButton *QAbstractButtonPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZN22QAbstractButtonPrivate6q_funcEv(
    QAbstractButtonPrivate *self) {
  return self->q_func();
}

//  const QAbstractButton *QAbstractButtonPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractButton *ritual_ZNK22QAbstractButtonPrivate6q_funcEv(
    const QAbstractButtonPrivate *self) {
  return self->q_func();
}

//  QAbstractButtonPrivate::QAbstractButtonPrivate(QSizePolicy::ControlType
//      type)
extern "C" Q_DECL_EXPORT
QAbstractButtonPrivate *ritual_ZN22QAbstractButtonPrivateC1EN11QSizePolicy11ControlTypeE(
    QSizePolicy::ControlType type) {
  return new CuteQAbstractButtonPrivate(type);
}

//  void QAbstractButtonPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate4initEv(QAbstractButtonPrivate *self) {
  self->init();
}

//  void QAbstractButtonPrivate::click()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate5clickEv(
    QAbstractButtonPrivate *self) {
  self->click();
}

//  void QAbstractButtonPrivate::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate7refreshEv(
    QAbstractButtonPrivate *self) {
  self->refresh();
}

//  QList<QAbstractButton *> QAbstractButtonPrivate::queryButtonList() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK22QAbstractButtonPrivate15queryButtonListEv(
    const QAbstractButtonPrivate *self) {
  return new QList<QAbstractButton *>(self->queryButtonList());
}

//  QAbstractButton *QAbstractButtonPrivate::queryCheckedButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK22QAbstractButtonPrivate18queryCheckedButtonEv(
    const QAbstractButtonPrivate *self) {
  return self->queryCheckedButton();
}

//  void QAbstractButtonPrivate::notifyChecked()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate13notifyCheckedEv(
    QAbstractButtonPrivate *self) {
  self->notifyChecked();
}

//  void QAbstractButtonPrivate::fixFocusPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate14fixFocusPolicyEv(
    QAbstractButtonPrivate *self) {
  self->fixFocusPolicy();
}

//  void QAbstractButtonPrivate::emitPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate11emitPressedEv(
    QAbstractButtonPrivate *self) {
  self->emitPressed();
}

//  void QAbstractButtonPrivate::emitReleased()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate12emitReleasedEv(
    QAbstractButtonPrivate *self) {
  self->emitReleased();
}

//  void QAbstractButtonPrivate::emitClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate11emitClickedEv(
    QAbstractButtonPrivate *self) {
  self->emitClicked();
}

//  void QAbstractButtonPrivate::emitToggled(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractButtonPrivate11emitToggledEb(
    QAbstractButtonPrivate *self,
    bool checked) {
  self->emitToggled(checked);
}

//  QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State
//      state) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE(
    const QAbstractButtonPrivate *self,
    int state) {
  return static_cast<int>(
      self->styleButtonState(
          QFlags<QStyle::StateFlag>::fromInt(state)).toInt());
}

//  a Python function taken by a CuteQAbstractButtonPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractButtonPrivate(
    QAbstractButtonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractButtonPrivate *>(self)->take(key, call);
}

//  QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State
//      state) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9StateFlagEE(
    const QAbstractButtonPrivate *self,
    int state) {
  return static_cast<int>(
      self->QAbstractButtonPrivate::styleButtonState(
          QFlags<QStyle::StateFlag>::fromInt(state)).toInt());
}

#endif  // QT_CONFIG(abstractbutton)
