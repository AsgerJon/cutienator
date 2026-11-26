//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickgraphicsinfo_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickgraphicsinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickgraphicsinfo_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtGui/qopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 258, as _ZN18QQuickGraphicsInfo9setWindowEP12QQuickWindow
inline void QQuickGraphicsInfo::setWindow(QQuickWindow *window)
{
    if (m_window != window) {
        if (m_window) {
            disconnect(m_window, SIGNAL(sceneGraphInitialized()), this, SLOT(updateInfo()));
            disconnect(m_window, SIGNAL(sceneGraphInvalidated()), this, SLOT(updateInfo()));
        }
        if (window) {
            connect(window, SIGNAL(sceneGraphInitialized()), this, SLOT(updateInfo()));
            connect(window, SIGNAL(sceneGraphInvalidated()), this, SLOT(updateInfo()));
        }
        m_window = window;
    }
    updateInfo();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickGraphicsInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickGraphicsInfo10metaObjectEv(
    const QQuickGraphicsInfo *self) {
  return self->metaObject();
}

//  void *QQuickGraphicsInfo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickGraphicsInfo11qt_metacastEPKc(
    QQuickGraphicsInfo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphicsInfo::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickGraphicsInfo11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphicsInfo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickGraphicsInfo::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo24qt_qmlMarker_uncreatableEv(
    QQuickGraphicsInfo *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickGraphicsInfo::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo21qt_qmlMarker_attachedEv(
    QQuickGraphicsInfo *self) {
  self->qt_qmlMarker_attached();
}

//  GraphicsApi QQuickGraphicsInfo::api() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::GraphicsApi ritual_ZNK18QQuickGraphicsInfo3apiEv(
    const QQuickGraphicsInfo *self) {
  return self->api();
}

//  ShaderType QQuickGraphicsInfo::shaderType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderType ritual_ZNK18QQuickGraphicsInfo10shaderTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderType();
}

//  ShaderCompilationType QQuickGraphicsInfo::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderCompilationType ritual_ZNK18QQuickGraphicsInfo21shaderCompilationTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderCompilationType();
}

//  ShaderSourceType QQuickGraphicsInfo::shaderSourceType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderSourceType ritual_ZNK18QQuickGraphicsInfo16shaderSourceTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderSourceType();
}

//  int QQuickGraphicsInfo::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickGraphicsInfo12majorVersionEv(
    const QQuickGraphicsInfo *self) {
  return self->majorVersion();
}

//  int QQuickGraphicsInfo::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickGraphicsInfo12minorVersionEv(
    const QQuickGraphicsInfo *self) {
  return self->minorVersion();
}

//  OpenGLContextProfile QQuickGraphicsInfo::profile() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::OpenGLContextProfile ritual_ZNK18QQuickGraphicsInfo7profileEv(
    const QQuickGraphicsInfo *self) {
  return self->profile();
}

//  RenderableType QQuickGraphicsInfo::renderableType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::RenderableType ritual_ZNK18QQuickGraphicsInfo14renderableTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->renderableType();
}

//  void QQuickGraphicsInfo::apiChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo10apiChangedEv(QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "apiChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "apiChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo17shaderTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderCompilationTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo28shaderCompilationTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderCompilationTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderCompilationTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderSourceTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo23shaderSourceTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderSourceTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderSourceTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::majorVersionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo19majorVersionChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "majorVersionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "majorVersionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::minorVersionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo19minorVersionChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minorVersionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minorVersionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::profileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo14profileChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "profileChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "profileChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::renderableTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo21renderableTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "renderableTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "renderableTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::updateInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo10updateInfoEv(QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateInfo()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateInfo()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo9setWindowEP12QQuickWindow(
    QQuickGraphicsInfo *self,
    QQuickWindow *window) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setWindow(QQuickWindow *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setWindow(QQuickWindow *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&window)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
