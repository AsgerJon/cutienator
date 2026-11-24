//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  bool QSSGRenderGraphObject::isNodeType(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject10isNodeTypeENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isNodeType(type);
}

//  bool QSSGRenderGraphObject::isLight(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject7isLightENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isLight(type);
}

//  bool QSSGRenderGraphObject::isCamera(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject8isCameraENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isCamera(type);
}

//  bool QSSGRenderGraphObject::isMaterial(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject10isMaterialENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isMaterial(type);
}

//  bool QSSGRenderGraphObject::isTexture(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject9isTextureENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isTexture(type);
}

//  bool QSSGRenderGraphObject::isRenderable(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject12isRenderableENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isRenderable(type);
}

//  bool QSSGRenderGraphObject::isResource(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject10isResourceENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isResource(type);
}

//  bool QSSGRenderGraphObject::isExtension(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject11isExtensionENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isExtension(type);
}

//  bool QSSGRenderGraphObject::isUserType(Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderGraphObject10isUserTypeENS_4TypeE(
    QSSGRenderGraphObject::Type type) {
  return QSSGRenderGraphObject::isUserType(type);
}

//  bool QSSGRenderGraphObject::hasGraphicsResources() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGRenderGraphObject20hasGraphicsResourcesEv(
    const QSSGRenderGraphObject *self) {
  return self->hasGraphicsResources();
}

//  QSSGRenderGraphObject::~QSSGRenderGraphObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderGraphObjectD1Ev(QSSGRenderGraphObject *self) {
  delete self;
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug stream, QSSGRenderGraphObject::Type type)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugN21QSSGRenderGraphObject4TypeE(
    const QDebug *stream,
    QSSGRenderGraphObject::Type type) {
  return new QDebug(operator<<(*stream, type));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QSSGRenderGraphObject::QSSGRenderGraphObject(QSSGRenderGraphObject::Type
//      inType)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QSSGRenderGraphObjectC1ENS_4TypeE(
    QSSGRenderGraphObject::Type inType) {
  return new QSSGRenderGraphObject(inType);
}

//  QSSGRenderGraphObject::QSSGRenderGraphObject(QSSGRenderGraphObject::Type
//      inType, FlagT inFlags)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QSSGRenderGraphObjectC1ENS_4TypeEj(
    QSSGRenderGraphObject::Type inType,
    QSSGRenderGraphObject::FlagT inFlags) {
  return new QSSGRenderGraphObject(inType, inFlags);
}

//  QList<QSSGRenderGraphObject *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSSGRenderGraphObject *> *ritual_list_make_QSSGRenderGraphObject_ptr() {
  return new QList<QSSGRenderGraphObject *>();
}

//  void QList<QSSGRenderGraphObject *>::append(const QSSGRenderGraphObject *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSSGRenderGraphObject_ptr(
    QList<QSSGRenderGraphObject *> *self,
    QSSGRenderGraphObject *element) {
  self->append(element);
}

//  qsizetype QList<QSSGRenderGraphObject *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSSGRenderGraphObject_ptr(
    const QList<QSSGRenderGraphObject *> *self) {
  return self->size();
}

//  const QSSGRenderGraphObject * &QList<QSSGRenderGraphObject
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_list_at_QSSGRenderGraphObject_ptr(
    const QList<QSSGRenderGraphObject *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSSGRenderGraphObject *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSSGRenderGraphObject_ptr(
    QList<QSSGRenderGraphObject *> *self) {
  delete self;
}
