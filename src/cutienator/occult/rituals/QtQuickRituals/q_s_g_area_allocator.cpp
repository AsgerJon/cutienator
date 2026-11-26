//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgareaallocator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgareaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qpoint.h>

//  QSGAreaAllocator::QSGAreaAllocator(const QSize &size)
extern "C" Q_DECL_EXPORT
QSGAreaAllocator *ritual_ZN16QSGAreaAllocatorC1ERK5QSize(const QSize *size) {
  return new QSGAreaAllocator(*size);
}

//  QSGAreaAllocator::~QSGAreaAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGAreaAllocatorD1Ev(QSGAreaAllocator *self) {
  delete self;
}

//  QRect QSGAreaAllocator::allocate(const QSize &size)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN16QSGAreaAllocator8allocateERK5QSize(
    QSGAreaAllocator *self,
    const QSize *size) {
  return new QRect(self->allocate(*size));
}

//  bool QSGAreaAllocator::deallocate(const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGAreaAllocator10deallocateERK5QRect(
    QSGAreaAllocator *self,
    const QRect *rect) {
  return self->deallocate(*rect);
}

//  bool QSGAreaAllocator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGAreaAllocator7isEmptyEv(const QSGAreaAllocator *self) {
  return self->isEmpty();
}

//  QSize QSGAreaAllocator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QSGAreaAllocator4sizeEv(const QSGAreaAllocator *self) {
  return new QSize(self->size());
}

//  QByteArray QSGAreaAllocator::serialize()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QSGAreaAllocator9serializeEv(QSGAreaAllocator *self) {
  return new QByteArray(self->serialize());
}

//  const char *QSGAreaAllocator::deserialize(const char *data, int size)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN16QSGAreaAllocator11deserializeEPKci(
    QSGAreaAllocator *self,
    const char *data,
    int size) {
  return self->deserialize(data, size);
}

//  bool QSGAreaAllocator::allocateInNode(const QSize &size, QPoint &result,
//      const QRect &currentRect, QSGAreaAllocatorNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGAreaAllocator14allocateInNodeERK5QSizeR6QPointRK5QRectP20QSGAreaAllocatorNode(
    QSGAreaAllocator *self,
    const QSize *size,
    QPoint *result,
    const QRect *currentRect,
    QSGAreaAllocatorNode *node) {
  return self->allocateInNode(*size, *result, *currentRect, node);
}

//  bool QSGAreaAllocator::deallocateInNode(const QPoint &pos,
//      QSGAreaAllocatorNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGAreaAllocator16deallocateInNodeERK6QPointP20QSGAreaAllocatorNode(
    QSGAreaAllocator *self,
    const QPoint *pos,
    QSGAreaAllocatorNode *node) {
  return self->deallocateInNode(*pos, node);
}

//  void QSGAreaAllocator::mergeNodeWithNeighbors(QSGAreaAllocatorNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGAreaAllocator22mergeNodeWithNeighborsEP20QSGAreaAllocatorNode(
    QSGAreaAllocator *self,
    QSGAreaAllocatorNode *node) {
  self->mergeNodeWithNeighbors(node);
}
