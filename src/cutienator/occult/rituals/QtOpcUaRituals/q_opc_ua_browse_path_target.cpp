//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuabrowsepathtarget.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuabrowsepathtarget.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtCore/qlist.h>

//  QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget()
extern "C" Q_DECL_EXPORT
QOpcUaBrowsePathTarget *ritual_ZN22QOpcUaBrowsePathTargetC1Ev() {
  return new QOpcUaBrowsePathTarget();
}

//  QOpcUaBrowsePathTarget::QOpcUaBrowsePathTarget(const
//      QOpcUaBrowsePathTarget &a0)
extern "C" Q_DECL_EXPORT
QOpcUaBrowsePathTarget *ritual_ZN22QOpcUaBrowsePathTargetC1ERKS_(
    const QOpcUaBrowsePathTarget *a0) {
  return new QOpcUaBrowsePathTarget(*a0);
}

//  bool QOpcUaBrowsePathTarget::operator==(const QOpcUaBrowsePathTarget
//      &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QOpcUaBrowsePathTargeteqERKS_(
    const QOpcUaBrowsePathTarget *self,
    const QOpcUaBrowsePathTarget *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaBrowsePathTarget::~QOpcUaBrowsePathTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaBrowsePathTargetD1Ev(QOpcUaBrowsePathTarget *self) {
  delete self;
}

//  QOpcUaExpandedNodeId QOpcUaBrowsePathTarget::targetId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK22QOpcUaBrowsePathTarget8targetIdEv(
    const QOpcUaBrowsePathTarget *self) {
  return new QOpcUaExpandedNodeId(self->targetId());
}

//  void QOpcUaBrowsePathTarget::setTargetId(const QOpcUaExpandedNodeId
//      &targetId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaBrowsePathTarget11setTargetIdERK20QOpcUaExpandedNodeId(
    QOpcUaBrowsePathTarget *self,
    const QOpcUaExpandedNodeId *targetId) {
  self->setTargetId(*targetId);
}

//  quint32 QOpcUaBrowsePathTarget::remainingPathIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK22QOpcUaBrowsePathTarget18remainingPathIndexEv(
    const QOpcUaBrowsePathTarget *self) {
  return self->remainingPathIndex();
}

//  void QOpcUaBrowsePathTarget::setRemainingPathIndex(quint32
//      remainingPathIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaBrowsePathTarget21setRemainingPathIndexEj(
    QOpcUaBrowsePathTarget *self,
    quint32 remainingPathIndex) {
  self->setRemainingPathIndex(remainingPathIndex);
}

//  bool QOpcUaBrowsePathTarget::isFullyResolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QOpcUaBrowsePathTarget15isFullyResolvedEv(
    const QOpcUaBrowsePathTarget *self) {
  return self->isFullyResolved();
}

//  QList<QOpcUaBrowsePathTarget>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaBrowsePathTarget> *ritual_list_make_QOpcUaBrowsePathTarget() {
  return new QList<QOpcUaBrowsePathTarget>();
}

//  void QList<QOpcUaBrowsePathTarget>::append(const QOpcUaBrowsePathTarget
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaBrowsePathTarget(
    QList<QOpcUaBrowsePathTarget> *self,
    const QOpcUaBrowsePathTarget *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaBrowsePathTarget>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaBrowsePathTarget(
    const QList<QOpcUaBrowsePathTarget> *self) {
  return self->size();
}

//  const QOpcUaBrowsePathTarget &QList<QOpcUaBrowsePathTarget>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QOpcUaBrowsePathTarget *ritual_list_at_QOpcUaBrowsePathTarget(
    const QList<QOpcUaBrowsePathTarget> *self,
    long long index) {
  return new QOpcUaBrowsePathTarget(self->at(index));
}

//  QList<QOpcUaBrowsePathTarget>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaBrowsePathTarget(
    QList<QOpcUaBrowsePathTarget> *self) {
  delete self;
}
