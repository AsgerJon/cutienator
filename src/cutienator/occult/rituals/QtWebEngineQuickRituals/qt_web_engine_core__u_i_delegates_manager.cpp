//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/ui_delegates_manager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/ui_delegates_manager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/ui_delegates_manager_p.h>
#include <QtCore/qdiriterator.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlist.h>
#include <QtCore/qtimer.h>
#include <QtGui/qcursor.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qscreen.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlproperty.h>
#include <QtQuick/qquickwindow.h>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtwebengine/src/webenginequick/ui_delegates_manager.cpp, line 781, as _ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject
namespace QtWebEngineCore {
using namespace Qt::Literals::StringLiterals;
inline void UIDelegatesManager::showMenu(QObject *menu)
{
    QMetaObject::invokeMethod(menu, "open");
}
}  // namespace QtWebEngineCore
//  -----------------------------------------------------------------------

//  A QtWebEngineCore::UIDelegatesManager that Python can take functions over in. Every QtWebEngineCore::UIDelegatesManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtWebEngineCore_UIDelegatesManagerCall0)(const void *, QQuickWebEngineAction *, QObject *, bool, bool, int *);
typedef void * (*CuteQtWebEngineCore_UIDelegatesManagerCall1)(const void *, QObject *, const QString *, const QPoint *, int *);
typedef void (*CuteQtWebEngineCore_UIDelegatesManagerCall2)(const void *, QObject *, int *);
class CuteQtWebEngineCore_UIDelegatesManager : public QtWebEngineCore::UIDelegatesManager {
public:
  using QtWebEngineCore::UIDelegatesManager::UIDelegatesManager;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QtWebEngineCore18UIDelegatesManager11addMenuItemEP21QQuickWebEngineActionP7QObjectbb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QtWebEngineCore18UIDelegatesManager7addMenuEP7QObjectRK7QStringRK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QtWebEngineCore::UIDelegatesManager::addMenuItem(QQuickWebEngine
  //      Action *action, QObject *menu, bool checkable, bool checked)
  void addMenuItem(
      QQuickWebEngineAction *action,
      QObject *menu,
      bool checkable,
      bool checked) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWebEngineCore_UIDelegatesManagerCall0 call = reinterpret_cast<CuteQtWebEngineCore_UIDelegatesManagerCall0>(taken[0]);
      call(this, action, menu, checkable, checked, &handled);
      if (handled) return;
    }
    QtWebEngineCore::UIDelegatesManager::addMenuItem(action, menu, checkable, checked);
  }

  //  QObject *QtWebEngineCore::UIDelegatesManager::addMenu(QObject
  //      *parentMenu, const QString &title, const QPoint &pos)
  QObject *addMenu(
      QObject *parentMenu,
      const QString &title,
      const QPoint &pos) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWebEngineCore_UIDelegatesManagerCall1 call = reinterpret_cast<CuteQtWebEngineCore_UIDelegatesManagerCall1>(taken[1]);
      void * given = call(this, parentMenu, &title, &pos, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QtWebEngineCore::UIDelegatesManager::addMenu(parentMenu, title, pos);
  }

  //  void QtWebEngineCore::UIDelegatesManager::showMenu(QObject *menu)
  void showMenu(QObject *menu) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWebEngineCore_UIDelegatesManagerCall2 call = reinterpret_cast<CuteQtWebEngineCore_UIDelegatesManagerCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QtWebEngineCore::UIDelegatesManager::showMenu(menu);
  }
};

//  QString QtWebEngineCore::UIDelegatesManager::tr(const char *sourceText,
//      const char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QtWebEngineCore18UIDelegatesManager2trEPKcS2_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QtWebEngineCore::UIDelegatesManager::tr(
          sourceText,
          disambiguation,
          n));
}

//  QtWebEngineCore::UIDelegatesManager::~UIDelegatesManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtWebEngineCore18UIDelegatesManagerD1Ev(
    QtWebEngineCore::UIDelegatesManager *self) {
  delete self;
}

//  void
//      QtWebEngineCore::UIDelegatesManager::addMenuItem(QQuickWebEngineActio
//      n *action, QObject *menu, bool checkable, bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtWebEngineCore18UIDelegatesManager11addMenuItemEP21QQuickWebEngineActionP7QObjectbb(
    QtWebEngineCore::UIDelegatesManager *self,
    QQuickWebEngineAction *action,
    QObject *menu,
    bool checkable,
    bool checked) {
  self->addMenuItem(action, menu, checkable, checked);
}

//  QObject *QtWebEngineCore::UIDelegatesManager::addMenu(QObject
//      *parentMenu, const QString &title, const QPoint &pos)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN15QtWebEngineCore18UIDelegatesManager7addMenuEP7QObjectRK7QStringRK6QPoint(
    QtWebEngineCore::UIDelegatesManager *self,
    QObject *parentMenu,
    const QString *title,
    const QPoint *pos) {
  return self->addMenu(parentMenu, *title, *pos);
}

//  void QtWebEngineCore::UIDelegatesManager::showMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject(
    QtWebEngineCore::UIDelegatesManager *self,
    QObject *menu) {
  self->showMenu(menu);
}

//  a Python function taken by a CuteQtWebEngineCore_UIDelegatesManager, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWebEngineCore_UIDelegatesManager(
    QtWebEngineCore::UIDelegatesManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWebEngineCore_UIDelegatesManager *>(self)->take(key, call);
}

//  void QtWebEngineCore::UIDelegatesManager::showMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject(
    QtWebEngineCore::UIDelegatesManager *self,
    QObject *menu) {
  self->QtWebEngineCore::UIDelegatesManager::showMenu(menu);
}
