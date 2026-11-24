//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelplink.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelplink.h>
#include <QtCore/qlist.h>

//  QHelpLink::~QHelpLink()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHelpLinkD1Ev(QHelpLink *self) {
  delete self;
}

//  QList<QHelpLink>::QList()
extern "C" Q_DECL_EXPORT
QList<QHelpLink> *ritual_list_make_QHelpLink() {
  return new QList<QHelpLink>();
}

//  void QList<QHelpLink>::append(const QHelpLink &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHelpLink(
    QList<QHelpLink> *self,
    const QHelpLink *element) {
  self->append(*element);
}

//  qsizetype QList<QHelpLink>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHelpLink(const QList<QHelpLink> *self) {
  return self->size();
}

//  const QHelpLink &QList<QHelpLink>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHelpLink *ritual_list_at_QHelpLink(
    const QList<QHelpLink> *self,
    long long index) {
  return new QHelpLink(self->at(index));
}

//  QList<QHelpLink>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHelpLink(QList<QHelpLink> *self) {
  delete self;
}
