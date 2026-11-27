//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 120, as _ZN29QWebEngineHistoryModelPrivateD2Ev
inline QWebEngineHistoryModelPrivate::~QWebEngineHistoryModelPrivate()
{
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 135, as _ZNK29QWebEngineHistoryModelPrivate5indexEi
inline int QWebEngineHistoryModelPrivate::index(int index) const
{
    return index;
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 124, as _ZNK29QWebEngineHistoryModelPrivate7adapterEv
inline QtWebEngineCore::WebContentsAdapter *QWebEngineHistoryModelPrivate::adapter() const
{
    Q_ASSERT(history->adapter());
    return history->adapter();
}
//  -----------------------------------------------------------------------

//  A QWebEngineHistoryModelPrivate that Python can take functions over in. Every QWebEngineHistoryModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQWebEngineHistoryModelPrivateCall0)(const void *, int *);
typedef int (*CuteQWebEngineHistoryModelPrivateCall1)(const void *, int, int *);
typedef int (*CuteQWebEngineHistoryModelPrivateCall2)(const void *, int, int *);
class CuteQWebEngineHistoryModelPrivate : public QWebEngineHistoryModelPrivate {
public:
  using QWebEngineHistoryModelPrivate::QWebEngineHistoryModelPrivate;
  CuteQWebEngineHistoryModelPrivate(const QWebEngineHistoryModelPrivate & other) : QWebEngineHistoryModelPrivate(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate5indexEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate14offsetForIndexEi")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  int QWebEngineHistoryModelPrivate::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineHistoryModelPrivateCall0 call = reinterpret_cast<CuteQWebEngineHistoryModelPrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWebEngineHistoryModelPrivate::count();
  }

  //  int QWebEngineHistoryModelPrivate::index(int a0) const
  int index(int a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineHistoryModelPrivateCall1 call = reinterpret_cast<CuteQWebEngineHistoryModelPrivateCall1>(taken[1]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEngineHistoryModelPrivate::index(a0);
  }

  //  int QWebEngineHistoryModelPrivate::offsetForIndex(int a0) const
  int offsetForIndex(int a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineHistoryModelPrivateCall2 call = reinterpret_cast<CuteQWebEngineHistoryModelPrivateCall2>(taken[2]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEngineHistoryModelPrivate::offsetForIndex(a0);
  }
};

//  QWebEngineHistoryModelPrivate::~QWebEngineHistoryModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWebEngineHistoryModelPrivateD1Ev(
    QWebEngineHistoryModelPrivate *self) {
  delete self;
}

//  int QWebEngineHistoryModelPrivate::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QWebEngineHistoryModelPrivate5countEv(
    const QWebEngineHistoryModelPrivate *self) {
  return self->count();
}

//  int QWebEngineHistoryModelPrivate::index(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QWebEngineHistoryModelPrivate5indexEi(
    const QWebEngineHistoryModelPrivate *self,
    int a0) {
  return self->index(a0);
}

//  int QWebEngineHistoryModelPrivate::offsetForIndex(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QWebEngineHistoryModelPrivate14offsetForIndexEi(
    const QWebEngineHistoryModelPrivate *self,
    int a0) {
  return self->offsetForIndex(a0);
}

//  QtWebEngineCore::WebContentsAdapter
//      *QWebEngineHistoryModelPrivate::adapter() const
extern "C" Q_DECL_EXPORT
QtWebEngineCore::WebContentsAdapter *ritual_ZNK29QWebEngineHistoryModelPrivate7adapterEv(
    const QWebEngineHistoryModelPrivate *self) {
  return self->adapter();
}

//  a Python function taken by a CuteQWebEngineHistoryModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineHistoryModelPrivate(
    QWebEngineHistoryModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineHistoryModelPrivate *>(self)->take(key, call);
}

//  int QWebEngineHistoryModelPrivate::index(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QWebEngineHistoryModelPrivate5indexEi(
    const QWebEngineHistoryModelPrivate *self,
    int a0) {
  return self->QWebEngineHistoryModelPrivate::index(a0);
}
