//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSSGRenderableObjectHandle::QSSGRenderableObjectHandle()
extern "C" Q_DECL_EXPORT
QSSGRenderableObjectHandle *ritual_ZN26QSSGRenderableObjectHandleC1Ev() {
  return new QSSGRenderableObjectHandle();
}

//  QSSGRenderableObjectHandle::QSSGRenderableObjectHandle(QSSGRenderableObje
//      ct *o, float camDistSq, QSSGRenderNodeTag tag)
extern "C" Q_DECL_EXPORT
QSSGRenderableObjectHandle *ritual_ZN26QSSGRenderableObjectHandleC1EP20QSSGRenderableObjectf14QSSGRenderFlag(
    QSSGRenderableObject *o,
    float camDistSq,
    const QSSGRenderFlag *tag) {
  return new QSSGRenderableObjectHandle(o, camDistSq, *tag);
}

//  QSSGRenderableObjectHandle::~QSSGRenderableObjectHandle()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderableObjectHandleD1Ev(
    QSSGRenderableObjectHandle *self) {
  delete self;
}

//  QList<QSSGRenderableObjectHandle>::QList()
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_list_make_QSSGRenderableObjectHandle() {
  return new QList<QSSGRenderableObjectHandle>();
}

//  void QList<QSSGRenderableObjectHandle>::append(const
//      QSSGRenderableObjectHandle &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSSGRenderableObjectHandle(
    QList<QSSGRenderableObjectHandle> *self,
    const QSSGRenderableObjectHandle *element) {
  self->append(*element);
}

//  qsizetype QList<QSSGRenderableObjectHandle>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSSGRenderableObjectHandle(
    const QList<QSSGRenderableObjectHandle> *self) {
  return self->size();
}

//  const QSSGRenderableObjectHandle
//      &QList<QSSGRenderableObjectHandle>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSSGRenderableObjectHandle *ritual_list_at_QSSGRenderableObjectHandle(
    const QList<QSSGRenderableObjectHandle> *self,
    long long index) {
  return new QSSGRenderableObjectHandle(self->at(index));
}

//  QList<QSSGRenderableObjectHandle>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSSGRenderableObjectHandle(
    QList<QSSGRenderableObjectHandle> *self) {
  delete self;
}
