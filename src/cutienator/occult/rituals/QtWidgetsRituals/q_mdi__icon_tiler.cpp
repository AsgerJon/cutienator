//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  void QMdi::IconTiler::rearrange(QList<QWidget *> &widgets, const QRect
//      &domain) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QMdi9IconTiler9rearrangeER5QListIP7QWidgetERK5QRect(
    const QMdi::IconTiler *self,
    QList<QWidget *> *widgets,
    const QRect *domain) {
  self->rearrange(*widgets, *domain);
}

//  Type QMdi::IconTiler::type() const
extern "C" Q_DECL_EXPORT
QMdi::Rearranger::Type ritual_ZNK4QMdi9IconTiler4typeEv(
    const QMdi::IconTiler *self) {
  return self->type();
}

//  QMdi::IconTiler::~IconTiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi9IconTilerD1Ev(QMdi::IconTiler *self) {
  delete self;
}

//  Type QMdi::IconTiler::type() const
extern "C" Q_DECL_EXPORT
QMdi::Rearranger::Type ritual_own_ZNK4QMdi9IconTiler4typeEv(
    const QMdi::IconTiler *self) {
  return self->QMdi::IconTiler::type();
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
