//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineview_p.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtCore/QPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#include <QtWebEngineQuick/qquickwebengineprofile.h>
#include <QtWebEngineQuick/private/qquickwebenginesettings_p.h>
#include <QtCore/qmimedatabase.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtCore/QThread>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginequick/api/qquickwebenginefaviconprovider.cpp, line 128, as _ZN21FaviconImageRequester24getNextViewForProcessingEv
inline QPointer<QQuickWebEngineView> FaviconImageRequester::getNextViewForProcessing()
{
    Q_ASSERT(QThread::currentThread() == QCoreApplication::instance()->thread());

    for (QPointer<QQuickWebEngineView> view : FaviconProviderHelper::instance()->views()) {
        if (view.isNull())
            continue;
        if (view->profile()->isOffTheRecord())
            continue;
        if (m_processedViews.contains(view))
            continue;
        m_processedViews.append(view);
        return view;
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *FaviconImageRequester::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21FaviconImageRequester10metaObjectEv(
    const FaviconImageRequester *self) {
  return self->metaObject();
}

//  void *FaviconImageRequester::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21FaviconImageRequester11qt_metacastEPKc(
    FaviconImageRequester *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int FaviconImageRequester::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21FaviconImageRequester11qt_metacallEN11QMetaObject4CallEiPPv(
    FaviconImageRequester *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void FaviconImageRequester::iconRequestDone(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconImageRequester15iconRequestDoneERK5QIcon(
    FaviconImageRequester *self,
    const QIcon *icon) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "FaviconImageRequester")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "iconRequestDone(const QIcon &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "iconRequestDone(const QIcon &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(icon)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void FaviconImageRequester::done(QPixmap pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN21FaviconImageRequester4doneE7QPixmap(
    FaviconImageRequester *self,
    const QPixmap *pixmap) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "FaviconImageRequester")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "done(QPixmap)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "done(QPixmap)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(pixmap)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QPointer<QQuickWebEngineView> a ritual of FaviconImageRequester gave
extern "C" Q_DECL_EXPORT
void ritual_drop_FaviconImageRequester__QPointer_QQuickWebEngineView(
    QPointer<QQuickWebEngineView> *self) {
  delete self;
}
