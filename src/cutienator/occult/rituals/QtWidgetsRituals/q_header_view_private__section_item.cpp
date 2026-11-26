//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qheaderview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qheaderview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHeaderViewPrivate::SectionItem::SectionItem()
extern "C" Q_DECL_EXPORT
QHeaderViewPrivate::SectionItem *ritual_ZN18QHeaderViewPrivate11SectionItemC1Ev() {
  return new QHeaderViewPrivate::SectionItem();
}

//  QHeaderViewPrivate::SectionItem::SectionItem(int length,
//      QHeaderView::ResizeMode mode)
extern "C" Q_DECL_EXPORT
QHeaderViewPrivate::SectionItem *ritual_ZN18QHeaderViewPrivate11SectionItemC1EiN11QHeaderView10ResizeModeE(
    int length,
    QHeaderView::ResizeMode mode) {
  return new QHeaderViewPrivate::SectionItem(length, mode);
}

//  int QHeaderViewPrivate::SectionItem::sectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate11SectionItem11sectionSizeEv(
    const QHeaderViewPrivate::SectionItem *self) {
  return self->sectionSize();
}

//  int QHeaderViewPrivate::SectionItem::calculatedEndPos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate11SectionItem16calculatedEndPosEv(
    const QHeaderViewPrivate::SectionItem *self) {
  return self->calculatedEndPos();
}

#if !defined(QT_NO_DATASTREAM)
//  void QHeaderViewPrivate::SectionItem::write(QDataStream &out) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QHeaderViewPrivate11SectionItem5writeER11QDataStream(
    const QHeaderViewPrivate::SectionItem *self,
    QDataStream *out) {
  self->write(*out);
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  void QHeaderViewPrivate::SectionItem::read(QDataStream &in)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate11SectionItem4readER11QDataStream(
    QHeaderViewPrivate::SectionItem *self,
    QDataStream *in) {
  self->read(*in);
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QHeaderViewPrivate::SectionItem::~SectionItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate11SectionItemD1Ev(
    QHeaderViewPrivate::SectionItem *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
