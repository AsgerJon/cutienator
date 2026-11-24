//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpcontentitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelpcontentitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  QHelpContentItem::~QHelpContentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHelpContentItemD1Ev(QHelpContentItem *self) {
  delete self;
}

//  QHelpContentItem *QHelpContentItem::child(int row) const
extern "C" Q_DECL_EXPORT
QHelpContentItem *ritual_ZNK16QHelpContentItem5childEi(
    const QHelpContentItem *self,
    int row) {
  return self->child(row);
}

//  int QHelpContentItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHelpContentItem10childCountEv(
    const QHelpContentItem *self) {
  return self->childCount();
}

//  QString QHelpContentItem::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QHelpContentItem5titleEv(const QHelpContentItem *self) {
  return new QString(self->title());
}

//  QUrl QHelpContentItem::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QHelpContentItem3urlEv(const QHelpContentItem *self) {
  return new QUrl(self->url());
}

//  int QHelpContentItem::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHelpContentItem3rowEv(const QHelpContentItem *self) {
  return self->row();
}

//  QHelpContentItem *QHelpContentItem::parent() const
extern "C" Q_DECL_EXPORT
QHelpContentItem *ritual_ZNK16QHelpContentItem6parentEv(
    const QHelpContentItem *self) {
  return self->parent();
}

//  int QHelpContentItem::childPosition(QHelpContentItem *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHelpContentItem13childPositionEPS_(
    const QHelpContentItem *self,
    QHelpContentItem *child) {
  return self->childPosition(child);
}

//  QHelpContentItem::QHelpContentItem(const QString &name, const QUrl &link,
//      QHelpContentItem *parent)
extern "C" Q_DECL_EXPORT
QHelpContentItem *ritual_ZN16QHelpContentItemC1ERK7QStringRK4QUrlPS_(
    const QString *name,
    const QUrl *link,
    QHelpContentItem *parent) {
  return new QHelpContentItem(*name, *link, parent);
}
