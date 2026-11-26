//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qapplication_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/qglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpixmap.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qabstracteventdispatcher.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qcursor.h>
#include <QtCore/qdir.h>
#include <QtGui/qevent.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#endif
#include <QtCore/qhash.h>
#include <QtCore/qset.h>
#include <QtWidgets/qlayout.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylefactory.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtCore/qtranslator.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/qwidget.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/private/qdnd_p.h>
#endif
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(style_stylesheet)
#include <QtWidgets/private/qstylesheetstyle_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/QWhatsThis>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible_base.h>
#include <QtWidgets/private/qaccessiblewidgetfactory_p.h>
#endif
#include <QtGui/private/qkeymapper_p.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qfont_p.h>
#if QT_CONFIG(action)
#include <QtGui/private/qaction_p.h>
#endif
#include <stdlib.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/qgesture.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtGui/qpa/qplatformfontdatabase.h>
#include <QtCore/qdatetime.h>
#include <QtGui/qpa/qplatformwindow.h>
#ifdef Q_OS_MACOS
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <algorithm>
#include <iterator>
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

//  from src/widgets/kernel/qapplication.cpp, line 340, as _ZN19QApplicationPrivate7isAlienEP7QWidget
inline bool QApplicationPrivate::isAlien(QWidget *widget)
{
    return widget && !widget->isWindow();
}
//  -----------------------------------------------------------------------

//  Only a class built on QApplicationPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQApplicationPrivate : QApplicationPrivate {
  using QApplicationPrivate::handleThemeChanged;
  using QApplicationPrivate::basePalette;
  using QApplicationPrivate::notifyDragStarted;
};

//  A QApplicationPrivate that Python can take functions over in. Every QApplicationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQApplicationPrivateCall0)(const void *, int *);
typedef void (*CuteQApplicationPrivateCall1)(const void *, QWindow *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQApplicationPrivateCall2)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQApplicationPrivateCall3)(const void *, int *);
#if !defined(QT_NO_ACTION)
typedef void * (*CuteQApplicationPrivateCall4)(const void *, int *);
#endif  // !defined(QT_NO_ACTION)
#if !defined(QT_NO_SHORTCUT)
typedef void * (*CuteQApplicationPrivateCall5)(const void *, int *);
#endif  // !defined(QT_NO_SHORTCUT)
typedef int (*CuteQApplicationPrivateCall6)(const void *, int *);
typedef bool (*CuteQApplicationPrivateCall7)(const void *, QWindow *, int *);
typedef void (*CuteQApplicationPrivateCall8)(const void *, int *);
typedef const QPalette * (*CuteQApplicationPrivateCall9)(const void *, int *);
#if QT_CONFIG(draganddrop)
typedef void (*CuteQApplicationPrivateCall10)(const void *, const QDrag *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef const QPixmap * (*CuteQApplicationPrivateCall11)(const void *, int, const QPixmap *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQApplicationPrivateCall12)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(commandlineparser)
typedef void (*CuteQApplicationPrivateCall13)(const void *, QList<QCommandLineOption> *, int *);
#endif  // QT_CONFIG(commandlineparser)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQApplicationPrivateCall14)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQApplicationPrivateCall15)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQApplicationPrivate : public QApplicationPrivate {
public:
  using QApplicationPrivate::QApplicationPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWindow")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate21createEventDispatcherEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate19createActionPrivateEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if !defined(QT_NO_SHORTCUT)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_SHORTCUT)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate15defaultModalityEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate18handleThemeChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate11basePaletteEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(commandlineparser)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate12addQtOptionsEP5QListI18QCommandLineOptionE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(commandlineparser)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate4quitEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QApplicationPrivate::notifyLayoutDirectionChange()
  void notifyLayoutDirectionChange() override {
    if (taken[0]) {
      int handled = 0;
      CuteQApplicationPrivateCall0 call = reinterpret_cast<CuteQApplicationPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QApplicationPrivate::notifyLayoutDirectionChange();
  }

  //  void QApplicationPrivate::notifyActiveWindowChange(QWindow *a0)
  void notifyActiveWindowChange(QWindow *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQApplicationPrivateCall1 call = reinterpret_cast<CuteQApplicationPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QApplicationPrivate::notifyActiveWindowChange(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QApplicationPrivate::createEventDispatcher()
  void createEventDispatcher() override {
    if (taken[2]) {
      int handled = 0;
      CuteQApplicationPrivateCall2 call = reinterpret_cast<CuteQApplicationPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QApplicationPrivate::createEventDispatcher();
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QApplicationPrivate::notifyWindowIconChanged()
  void notifyWindowIconChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQApplicationPrivateCall3 call = reinterpret_cast<CuteQApplicationPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QApplicationPrivate::notifyWindowIconChanged();
  }

#if !defined(QT_NO_ACTION)
  //  QActionPrivate *QApplicationPrivate::createActionPrivate() const
  QActionPrivate *createActionPrivate() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQApplicationPrivateCall4 call = reinterpret_cast<CuteQApplicationPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QActionPrivate *>(given);
    }
    return QApplicationPrivate::createActionPrivate();
  }
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
  //  QShortcutPrivate *QApplicationPrivate::createShortcutPrivate() const
  QShortcutPrivate *createShortcutPrivate() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQApplicationPrivateCall5 call = reinterpret_cast<CuteQApplicationPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QShortcutPrivate *>(given);
    }
    return QApplicationPrivate::createShortcutPrivate();
  }
#endif  // !defined(QT_NO_SHORTCUT)

  //  Qt::WindowModality QApplicationPrivate::defaultModality() const
  Qt::WindowModality defaultModality() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQApplicationPrivateCall6 call = reinterpret_cast<CuteQApplicationPrivateCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::WindowModality>(given);
    }
    return QApplicationPrivate::defaultModality();
  }

  //  bool QApplicationPrivate::windowNeverBlocked(QWindow *window) const
  bool windowNeverBlocked(QWindow *window) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQApplicationPrivateCall7 call = reinterpret_cast<CuteQApplicationPrivateCall7>(taken[7]);
      bool given = call(this, window, &handled);
      if (handled) return given;
    }
    return QApplicationPrivate::windowNeverBlocked(window);
  }

  //  void QApplicationPrivate::handleThemeChanged()
  void handleThemeChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQApplicationPrivateCall8 call = reinterpret_cast<CuteQApplicationPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QApplicationPrivate::handleThemeChanged();
  }

  //  QPalette QApplicationPrivate::basePalette() const
  QPalette basePalette() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQApplicationPrivateCall9 call = reinterpret_cast<CuteQApplicationPrivateCall9>(taken[9]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QApplicationPrivate::basePalette();
  }

#if QT_CONFIG(draganddrop)
  //  void QApplicationPrivate::notifyDragStarted(const QDrag *a0)
  void notifyDragStarted(const QDrag *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQApplicationPrivateCall10 call = reinterpret_cast<CuteQApplicationPrivateCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QApplicationPrivate::notifyDragStarted(a0);
  }
#endif  // QT_CONFIG(draganddrop)

  //  QPixmap QApplicationPrivate::applyQIconStyleHelper(QIcon::Mode mode,
  //      const QPixmap &base) const
  QPixmap applyQIconStyleHelper(
      QIcon::Mode mode,
      const QPixmap &base) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQApplicationPrivateCall11 call = reinterpret_cast<CuteQApplicationPrivateCall11>(taken[11]);
      const QPixmap * given = call(this, static_cast<int>(mode), &base, &handled);
      if (handled && given) return *given;
    }
    return QApplicationPrivate::applyQIconStyleHelper(mode, base);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QGuiApplicationPrivate::eventDispatcherReady()
  void eventDispatcherReady() override {
    if (taken[12]) {
      int handled = 0;
      CuteQApplicationPrivateCall12 call = reinterpret_cast<CuteQApplicationPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::eventDispatcherReady();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(commandlineparser)
  //  void QGuiApplicationPrivate::addQtOptions(QList<QCommandLineOption>
  //      *options)
  void addQtOptions(QList<QCommandLineOption> *options) override {
    if (taken[13]) {
      int handled = 0;
      CuteQApplicationPrivateCall13 call = reinterpret_cast<CuteQApplicationPrivateCall13>(taken[13]);
      call(this, options, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::addQtOptions(options);
  }
#endif  // QT_CONFIG(commandlineparser)

#if !defined(QT_NO_QOBJECT)
  //  bool QGuiApplicationPrivate::canQuitAutomatically()
  bool canQuitAutomatically() override {
    if (taken[14]) {
      int handled = 0;
      CuteQApplicationPrivateCall14 call = reinterpret_cast<CuteQApplicationPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGuiApplicationPrivate::canQuitAutomatically();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QGuiApplicationPrivate::quit()
  void quit() override {
    if (taken[15]) {
      int handled = 0;
      CuteQApplicationPrivateCall15 call = reinterpret_cast<CuteQApplicationPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::quit();
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QApplication *QApplicationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QApplication *ritual_ZN19QApplicationPrivate6q_funcEv(
    QApplicationPrivate *self) {
  return self->q_func();
}

//  const QApplication *QApplicationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QApplication *ritual_ZNK19QApplicationPrivate6q_funcEv(
    const QApplicationPrivate *self) {
  return self->q_func();
}

//  QApplicationPrivate::QApplicationPrivate(int &argc, char **argv)
extern "C" Q_DECL_EXPORT
QApplicationPrivate *ritual_ZN19QApplicationPrivateC1ERiPPc(
    int *argc,
    char **argv) {
  return new CuteQApplicationPrivate(*argc, argv);
}

//  QApplicationPrivate::~QApplicationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivateD1Ev(QApplicationPrivate *self) {
  delete self;
}

//  void QApplicationPrivate::notifyLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate27notifyLayoutDirectionChangeEv(
    QApplicationPrivate *self) {
  self->notifyLayoutDirectionChange();
}

//  void QApplicationPrivate::notifyActiveWindowChange(QWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate24notifyActiveWindowChangeEP7QWindow(
    QApplicationPrivate *self,
    QWindow *a0) {
  self->notifyActiveWindowChange(a0);
}

//  QString QApplicationPrivate::desktopStyleKey()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QApplicationPrivate15desktopStyleKeyEv() {
  return new QString(QApplicationPrivate::desktopStyleKey());
}

//  void QApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate21createEventDispatcherEv(
    QApplicationPrivate *self) {
  self->createEventDispatcher();
}

//  void QApplicationPrivate::dispatchEnterLeave(QWidget *enter, QWidget
//      *leave, const QPointF &globalPosF)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate18dispatchEnterLeaveEP7QWidgetS1_RK7QPointF(
    QWidget *enter,
    QWidget *leave,
    const QPointF *globalPosF) {
  QApplicationPrivate::dispatchEnterLeave(enter, leave, *globalPosF);
}

//  void QApplicationPrivate::notifyWindowIconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate23notifyWindowIconChangedEv(
    QApplicationPrivate *self) {
  self->notifyWindowIconChanged();
}

//  bool QApplicationPrivate::compressEvent(QEvent *event, QObject *receiver,
//      QPostEventList *postedEvents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate13compressEventEP6QEventP7QObjectP14QPostEventList(
    QApplicationPrivate *self,
    QEvent *event,
    QObject *receiver,
    QPostEventList *postedEvents) {
  return self->compressEvent(event, receiver, postedEvents);
}

#if !defined(QT_NO_ACTION)
//  QActionPrivate *QApplicationPrivate::createActionPrivate() const
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_ZNK19QApplicationPrivate19createActionPrivateEv(
    const QApplicationPrivate *self) {
  return self->createActionPrivate();
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
//  QShortcutPrivate *QApplicationPrivate::createShortcutPrivate() const
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_ZNK19QApplicationPrivate21createShortcutPrivateEv(
    const QApplicationPrivate *self) {
  return self->createShortcutPrivate();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  Qt::WindowModality QApplicationPrivate::defaultModality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK19QApplicationPrivate15defaultModalityEv(
    const QApplicationPrivate *self) {
  return self->defaultModality();
}

//  bool QApplicationPrivate::windowNeverBlocked(QWindow *window) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QApplicationPrivate18windowNeverBlockedEP7QWindow(
    const QApplicationPrivate *self,
    QWindow *window) {
  return self->windowNeverBlocked(window);
}

//  bool QApplicationPrivate::isBlockedByModal(QWidget *widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate16isBlockedByModalEP7QWidget(
    QWidget *widget) {
  return QApplicationPrivate::isBlockedByModal(widget);
}

//  bool QApplicationPrivate::modalState()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate10modalStateEv() {
  return QApplicationPrivate::modalState();
}

//  bool QApplicationPrivate::tryModalHelper(QWidget *widget, QWidget
//      **rettop)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate14tryModalHelperEP7QWidgetPS1_(
    QWidget *widget,
    QWidget **rettop) {
  return QApplicationPrivate::tryModalHelper(widget, rettop);
}

//  bool QApplicationPrivate::notify_helper(QObject *receiver, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate13notify_helperEP7QObjectP6QEvent(
    QApplicationPrivate *self,
    QObject *receiver,
    QEvent *e) {
  return self->notify_helper(receiver, e);
}

//  void QApplicationPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate4initEv(QApplicationPrivate *self) {
  self->init();
}

//  void QApplicationPrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate10initializeEv(
    QApplicationPrivate *self) {
  self->initialize();
}

//  void QApplicationPrivate::process_cmdline()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate15process_cmdlineEv(
    QApplicationPrivate *self) {
  self->process_cmdline();
}

//  void QApplicationPrivate::setActiveWindow(QWidget *act)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate15setActiveWindowEP7QWidget(
    QWidget *act) {
  QApplicationPrivate::setActiveWindow(act);
}

//  bool QApplicationPrivate::inPopupMode()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate11inPopupModeEv() {
  return QApplicationPrivate::inPopupMode();
}

//  void QApplicationPrivate::closePopup(QWidget *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate10closePopupEP7QWidget(
    QApplicationPrivate *self,
    QWidget *popup) {
  self->closePopup(popup);
}

//  void QApplicationPrivate::openPopup(QWidget *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate9openPopupEP7QWidget(
    QApplicationPrivate *self,
    QWidget *popup) {
  self->openPopup(popup);
}

//  void QApplicationPrivate::setFocusWidget(QWidget *focus, Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate14setFocusWidgetEP7QWidgetN2Qt11FocusReasonE(
    QWidget *focus,
    Qt::FocusReason reason) {
  QApplicationPrivate::setFocusWidget(focus, reason);
}

//  QWidget *QApplicationPrivate::focusNextPrevChild_helper(QWidget
//      *toplevel, bool next, bool *wrappingOccurred)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN19QApplicationPrivate25focusNextPrevChild_helperEP7QWidgetbPb(
    QWidget *toplevel,
    bool next,
    bool *wrappingOccurred) {
  return QApplicationPrivate::focusNextPrevChild_helper(
      toplevel,
      next,
      wrappingOccurred);
}

//  void QApplicationPrivate::handleThemeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate18handleThemeChangedEv(
    QApplicationPrivate *self) {
  self->handleThemeChanged();
}

//  QPalette QApplicationPrivate::basePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK19QApplicationPrivate11basePaletteEv(
    const QApplicationPrivate *self) {
  return new QPalette(self->basePalette());
}

//  void QApplicationPrivate::handlePaletteChanged(const char *className)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate20handlePaletteChangedEPKc(
    QApplicationPrivate *self,
    const char *className) {
  self->handlePaletteChanged(className);
}

#if QT_CONFIG(draganddrop)
//  void QApplicationPrivate::notifyDragStarted(const QDrag *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate17notifyDragStartedEPK5QDrag(
    QApplicationPrivate *self,
    const QDrag *a0) {
  self->notifyDragStarted(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QApplicationPrivate::initializeWidgetPalettesFromTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate33initializeWidgetPalettesFromThemeEv() {
  QApplicationPrivate::initializeWidgetPalettesFromTheme();
}

//  void QApplicationPrivate::initializeWidgetFontHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate24initializeWidgetFontHashEv() {
  QApplicationPrivate::initializeWidgetFontHash();
}

//  void QApplicationPrivate::setSystemFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate13setSystemFontERK5QFont(
    const QFont *font) {
  QApplicationPrivate::setSystemFont(*font);
}

//  QApplicationPrivate *QApplicationPrivate::instance()
extern "C" Q_DECL_EXPORT
QApplicationPrivate *ritual_ZN19QApplicationPrivate8instanceEv() {
  return QApplicationPrivate::instance();
}

//  QWidget *QApplicationPrivate::pickMouseReceiver(QWidget *candidate, const
//      QPointF &windowPos, QPointF *pos, QEvent::Type type, Qt::MouseButtons
//      buttons, QWidget *buttonDown, QWidget *alienWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN19QApplicationPrivate17pickMouseReceiverEP7QWidgetRK7QPointFPS2_N6QEvent4TypeE6QFlagsIN2Qt11MouseButtonEES1_S1_(
    QWidget *candidate,
    const QPointF *windowPos,
    QPointF *pos,
    QEvent::Type type,
    int buttons,
    QWidget *buttonDown,
    QWidget *alienWidget) {
  return QApplicationPrivate::pickMouseReceiver(
      candidate,
      *windowPos,
      pos,
      type,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      buttonDown,
      alienWidget);
}

//  bool QApplicationPrivate::sendMouseEvent(QWidget *receiver, QMouseEvent
//      *event, QWidget *alienWidget, QWidget *native, QWidget **buttonDown,
//      QPointer<QWidget> &lastMouseReceiver, bool spontaneous, bool
//      onlyDispatchEnterLeave)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate14sendMouseEventEP7QWidgetP11QMouseEventS1_S1_PS1_R8QPointerIS0_Ebb(
    QWidget *receiver,
    QMouseEvent *event,
    QWidget *alienWidget,
    QWidget *native,
    QWidget **buttonDown,
    QPointer<QWidget> *lastMouseReceiver,
    bool spontaneous,
    bool onlyDispatchEnterLeave) {
  return QApplicationPrivate::sendMouseEvent(
      receiver,
      event,
      alienWidget,
      native,
      buttonDown,
      *lastMouseReceiver,
      spontaneous,
      onlyDispatchEnterLeave);
}

//  void QApplicationPrivate::sendSyntheticEnterLeave(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate23sendSyntheticEnterLeaveEP7QWidget(
    QApplicationPrivate *self,
    QWidget *widget) {
  self->sendSyntheticEnterLeave(widget);
}

//  QWindow *QApplicationPrivate::windowForWidget(const QWidget *widget)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN19QApplicationPrivate15windowForWidgetEPK7QWidget(
    const QWidget *widget) {
  return QApplicationPrivate::windowForWidget(widget);
}

//  bool QApplicationPrivate::updateTouchPointsForWidget(QWidget *widget,
//      QTouchEvent *touchEvent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate26updateTouchPointsForWidgetEP7QWidgetP11QTouchEvent(
    QWidget *widget,
    QTouchEvent *touchEvent) {
  return QApplicationPrivate::updateTouchPointsForWidget(widget, touchEvent);
}

//  void QApplicationPrivate::initializeMultitouch()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate20initializeMultitouchEv(
    QApplicationPrivate *self) {
  self->initializeMultitouch();
}

//  void QApplicationPrivate::initializeMultitouch_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate24initializeMultitouch_sysEv(
    QApplicationPrivate *self) {
  self->initializeMultitouch_sys();
}

//  void QApplicationPrivate::cleanupMultitouch()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate17cleanupMultitouchEv(
    QApplicationPrivate *self) {
  self->cleanupMultitouch();
}

//  void QApplicationPrivate::cleanupMultitouch_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate21cleanupMultitouch_sysEv(
    QApplicationPrivate *self) {
  self->cleanupMultitouch_sys();
}

//  QWidget *QApplicationPrivate::findClosestTouchPointTarget(const
//      QPointingDevice *device, const QEventPoint &touchPoint)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN19QApplicationPrivate27findClosestTouchPointTargetEPK15QPointingDeviceRK11QEventPoint(
    QApplicationPrivate *self,
    const QPointingDevice *device,
    const QEventPoint *touchPoint) {
  return self->findClosestTouchPointTarget(device, *touchPoint);
}

//  void QApplicationPrivate::activateImplicitTouchGrab(QWidget *widget,
//      QTouchEvent *touchBeginEvent, ImplicitTouchGrabMode grabMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate25activateImplicitTouchGrabEP7QWidgetP11QTouchEventNS_21ImplicitTouchGrabModeE(
    QApplicationPrivate *self,
    QWidget *widget,
    QTouchEvent *touchBeginEvent,
    QApplicationPrivate::ImplicitTouchGrabMode grabMode) {
  self->activateImplicitTouchGrab(widget, touchBeginEvent, grabMode);
}

//  bool QApplicationPrivate::translateRawTouchEvent(QWidget *widget, const
//      QTouchEvent *touchEvent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate22translateRawTouchEventEP7QWidgetPK11QTouchEvent(
    QWidget *widget,
    const QTouchEvent *touchEvent) {
  return QApplicationPrivate::translateRawTouchEvent(widget, touchEvent);
}

//  void QApplicationPrivate::translateTouchCancel(const QPointingDevice
//      *device, ulong timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate20translateTouchCancelEPK15QPointingDevicem(
    const QPointingDevice *device,
    ulong timestamp) {
  QApplicationPrivate::translateTouchCancel(device, timestamp);
}

//  QPixmap QApplicationPrivate::applyQIconStyleHelper(QIcon::Mode mode,
//      const QPixmap &base) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK19QApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap(
    const QApplicationPrivate *self,
    QIcon::Mode mode,
    const QPixmap *base) {
  return new QPixmap(self->applyQIconStyleHelper(mode, *base));
}

//  bool QApplicationPrivate::tryCloseAllWidgetWindows(QWindowList
//      *processedWindows)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate24tryCloseAllWidgetWindowsEP5QListIP7QWindowE(
    QWindowList *processedWindows) {
  return QApplicationPrivate::tryCloseAllWidgetWindows(processedWindows);
}

//  void QApplicationPrivate::giveFocusAccordingToFocusPolicy(QWidget *w,
//      QEvent *event, QPoint localPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QApplicationPrivate31giveFocusAccordingToFocusPolicyEP7QWidgetP6QEvent6QPoint(
    QWidget *w,
    QEvent *event,
    const QPoint *localPos) {
  QApplicationPrivate::giveFocusAccordingToFocusPolicy(w, event, *localPos);
}

//  bool QApplicationPrivate::shouldSetFocus(QWidget *w, Qt::FocusPolicy
//      policy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate14shouldSetFocusEP7QWidgetN2Qt11FocusPolicyE(
    QWidget *w,
    Qt::FocusPolicy policy) {
  return QApplicationPrivate::shouldSetFocus(w, policy);
}

//  bool QApplicationPrivate::isAlien(QWidget *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QApplicationPrivate7isAlienEP7QWidget(QWidget *a0) {
  return QApplicationPrivate::isAlien(a0);
}

//  a Python function taken by a CuteQApplicationPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QApplicationPrivate(
    QApplicationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQApplicationPrivate *>(self)->take(key, call);
}

//  void QApplicationPrivate::notifyLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate27notifyLayoutDirectionChangeEv(
    QApplicationPrivate *self) {
  self->QApplicationPrivate::notifyLayoutDirectionChange();
}

//  void QApplicationPrivate::notifyActiveWindowChange(QWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate24notifyActiveWindowChangeEP7QWindow(
    QApplicationPrivate *self,
    QWindow *a0) {
  self->QApplicationPrivate::notifyActiveWindowChange(a0);
}

//  void QApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate21createEventDispatcherEv(
    QApplicationPrivate *self) {
  self->QApplicationPrivate::createEventDispatcher();
}

//  void QApplicationPrivate::notifyWindowIconChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate23notifyWindowIconChangedEv(
    QApplicationPrivate *self) {
  self->QApplicationPrivate::notifyWindowIconChanged();
}

#if !defined(QT_NO_ACTION)
//  QActionPrivate *QApplicationPrivate::createActionPrivate() const
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_own_ZNK19QApplicationPrivate19createActionPrivateEv(
    const QApplicationPrivate *self) {
  return self->QApplicationPrivate::createActionPrivate();
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
//  QShortcutPrivate *QApplicationPrivate::createShortcutPrivate() const
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_own_ZNK19QApplicationPrivate21createShortcutPrivateEv(
    const QApplicationPrivate *self) {
  return self->QApplicationPrivate::createShortcutPrivate();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  Qt::WindowModality QApplicationPrivate::defaultModality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_own_ZNK19QApplicationPrivate15defaultModalityEv(
    const QApplicationPrivate *self) {
  return self->QApplicationPrivate::defaultModality();
}

//  bool QApplicationPrivate::windowNeverBlocked(QWindow *window) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QApplicationPrivate18windowNeverBlockedEP7QWindow(
    const QApplicationPrivate *self,
    QWindow *window) {
  return self->QApplicationPrivate::windowNeverBlocked(window);
}

//  void QApplicationPrivate::handleThemeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate18handleThemeChangedEv(
    QApplicationPrivate *self) {
  static_cast<OwnQApplicationPrivate *>(self)->OwnQApplicationPrivate::handleThemeChanged();
}

//  QPalette QApplicationPrivate::basePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK19QApplicationPrivate11basePaletteEv(
    const QApplicationPrivate *self) {
  return new QPalette(
      static_cast<const OwnQApplicationPrivate *>(self)->OwnQApplicationPrivate::basePalette());
}

#if QT_CONFIG(draganddrop)
//  void QApplicationPrivate::notifyDragStarted(const QDrag *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QApplicationPrivate17notifyDragStartedEPK5QDrag(
    QApplicationPrivate *self,
    const QDrag *a0) {
  static_cast<OwnQApplicationPrivate *>(self)->OwnQApplicationPrivate::notifyDragStarted(
      a0);
}
#endif  // QT_CONFIG(draganddrop)

//  QPixmap QApplicationPrivate::applyQIconStyleHelper(QIcon::Mode mode,
//      const QPixmap &base) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK19QApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap(
    const QApplicationPrivate *self,
    QIcon::Mode mode,
    const QPixmap *base) {
  return new QPixmap(
      self->QApplicationPrivate::applyQIconStyleHelper(
          mode,
          *base));
}
