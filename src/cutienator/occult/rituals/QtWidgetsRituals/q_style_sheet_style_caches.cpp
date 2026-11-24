//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstylesheetstyle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstylesheetstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qglobal.h>
#include "qstylesheetstyle_p.h"
#if QT_CONFIG(style_stylesheet)
#include "private/qcssutil_p.h"
#include <qdebug.h>
#include <qdir.h>
#include <qapplication.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(menubar)
#include <qmenubar.h>
#endif
#include <qpainter.h>
#include <qstyleoption.h>
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#endif
#if QT_CONFIG(textedit)
#include <qtextedit.h>
#include <qplaintextedit.h>
#endif
#include <private/qwindowsstyle_p.h>
#if QT_CONFIG(combobox)
#include <qcombobox.h>
#endif
#include "private/qcssparser_p.h"
#include "private/qmath_p.h"
#include <qabstractscrollarea.h>
#include "private/qabstractscrollarea_p.h"
#if QT_CONFIG(tooltip)
#include "private/qtooltip_p.h"
#endif
#include <qshareddata.h>
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#if QT_CONFIG(scrollbar)
#include <qscrollbar.h>
#endif
#if QT_CONFIG(abstractslider)
#include <qabstractslider.h>
#endif
#include <qstring.h>
#include <qfile.h>
#if QT_CONFIG(checkbox)
#include <qcheckbox.h>
#endif
#if QT_CONFIG(itemviews)
#include <qheaderview.h>
#endif
#include <private/qwindowsstyle_p_p.h>
#if QT_CONFIG(animation)
#include <private/qstyleanimation_p.h>
#endif
#if QT_CONFIG(tabbar)
#include <private/qtabbar_p.h>
#endif
#include <QMetaProperty>
#if QT_CONFIG(mainwindow)
#include <qmainwindow.h>
#endif
#if QT_CONFIG(dockwidget)
#include <qdockwidget.h>
#endif
#if QT_CONFIG(mdiarea)
#include <qmdisubwindow.h>
#endif
#if QT_CONFIG(dialog)
#include <qdialog.h>
#endif
#include <private/qwidget_p.h>
#if QT_CONFIG(spinbox)
#include <QAbstractSpinBox>
#endif
#if QT_CONFIG(label)
#include <QLabel>
#endif
#include "qdrawutil.h"
#include "qstylehelper_p.h"
#include <limits.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#include <QtGui/qpainterpath.h>
#include <QtGui/qpainterstateguard.h>
#include <QtGui/qscreen.h>
#include <QtCore/private/qduplicatetracker_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/styles/qstylesheetstyle.cpp, line 2852, as _ZN22QStyleSheetStyleCaches14styleDestroyedEP7QObject
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyleCaches::styleDestroyed(QObject *o)
{
    styleSheetCache.remove(o);
}
#endif  // QT_CONFIG(style_stylesheet)
//  -----------------------------------------------------------------------

//  A QStyleSheetStyleCaches that Python can take functions over in. Every QStyleSheetStyleCaches
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleSheetStyleCachesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleSheetStyleCachesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCachesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCachesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCachesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCachesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCachesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStyleSheetStyleCaches : public QStyleSheetStyleCaches {
public:
  using QStyleSheetStyleCaches::QStyleSheetStyleCaches;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall0 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall1 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall2 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall3 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall4 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall5 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStyleSheetStyleCachesCall6 call = reinterpret_cast<CuteQStyleSheetStyleCachesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStyleSheetStyleCaches::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QStyleSheetStyleCaches10metaObjectEv(
    const QStyleSheetStyleCaches *self) {
  return self->metaObject();
}

#if QT_CONFIG(style_stylesheet)
//  void QStyleSheetStyleCaches::styleDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleSheetStyleCaches14styleDestroyedEP7QObject(
    QStyleSheetStyleCaches *self,
    QObject *a0) {
  self->styleDestroyed(a0);
}
#endif  // QT_CONFIG(style_stylesheet)

//  a Python function taken by a CuteQStyleSheetStyleCaches, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyleSheetStyleCaches(
    QStyleSheetStyleCaches *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStyleSheetStyleCaches *>(self)->take(key, call);
}

#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
