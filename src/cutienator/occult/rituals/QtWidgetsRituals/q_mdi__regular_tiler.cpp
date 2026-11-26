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

//  void QMdi::RegularTiler::rearrange(QList<QWidget *> &widgets, const QRect
//      &domain) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QMdi12RegularTiler9rearrangeER5QListIP7QWidgetERK5QRect(
    const QMdi::RegularTiler *self,
    QList<QWidget *> *widgets,
    const QRect *domain) {
  self->rearrange(*widgets, *domain);
}

//  Type QMdi::RegularTiler::type() const
extern "C" Q_DECL_EXPORT
QMdi::Rearranger::Type ritual_ZNK4QMdi12RegularTiler4typeEv(
    const QMdi::RegularTiler *self) {
  return self->type();
}

//  QMdi::RegularTiler::~RegularTiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi12RegularTilerD1Ev(QMdi::RegularTiler *self) {
  delete self;
}

//  Type QMdi::RegularTiler::type() const
extern "C" Q_DECL_EXPORT
QMdi::Rearranger::Type ritual_own_ZNK4QMdi12RegularTiler4typeEv(
    const QMdi::RegularTiler *self) {
  return self->QMdi::RegularTiler::type();
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
