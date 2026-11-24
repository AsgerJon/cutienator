//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::CETypes::EndPoint::EndPoint(Connection *_con, Type
//      _type)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CETypes::EndPoint *ritual_ZN18qdesigner_internal7CETypes8EndPointC1EPNS_10ConnectionENS1_4TypeE(
    qdesigner_internal::Connection *_con,
    qdesigner_internal::CETypes::EndPoint::Type _type) {
  return new qdesigner_internal::CETypes::EndPoint(_con, _type);
}

//  bool qdesigner_internal::CETypes::EndPoint::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal7CETypes8EndPoint6isNullEv(
    const qdesigner_internal::CETypes::EndPoint *self) {
  return self->isNull();
}

//  bool qdesigner_internal::CETypes::EndPoint::operator==(const EndPoint
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal7CETypes8EndPointeqERKS1_(
    const qdesigner_internal::CETypes::EndPoint *self,
    const qdesigner_internal::CETypes::EndPoint *other) {
  return self->operator==(*other);
}

//  bool qdesigner_internal::CETypes::EndPoint::operator!=(const EndPoint
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal7CETypes8EndPointneERKS1_(
    const qdesigner_internal::CETypes::EndPoint *self,
    const qdesigner_internal::CETypes::EndPoint *other) {
  return self->operator!=(*other);
}

//  qdesigner_internal::CETypes::EndPoint::~EndPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal7CETypes8EndPointD1Ev(
    qdesigner_internal::CETypes::EndPoint *self) {
  delete self;
}
