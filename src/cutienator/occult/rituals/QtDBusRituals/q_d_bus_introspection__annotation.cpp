//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintrospection_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QDBusIntrospection::Annotation::operator==(const Annotation &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDBusIntrospection10AnnotationeqERKS0_(
    const QDBusIntrospection::Annotation *self,
    const QDBusIntrospection::Annotation *other) {
  return self->operator==(*other);
}

//  QDBusIntrospection::Annotation::~Annotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDBusIntrospection10AnnotationD1Ev(
    QDBusIntrospection::Annotation *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
