//  Written by hand on 2026-11-25 from
//  QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/universalnode_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its inline
//  function 'createNodeString' and its virtual functions, called
//  through the object, are written.
//  Not written: the constructors, 'tr', 'operator=' and every other
//  function, which Qt's library offers not.
#include <QtOpcUa/qopcuaglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
#include <QtDeclarativeOpcua/6.12.0/QtDeclarativeOpcua/private/universalnode_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *UniversalNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13UniversalNode10metaObjectEv(
    const UniversalNode *self) {
  return self->metaObject();
}

//  UniversalNode::~UniversalNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13UniversalNodeD1Ev(UniversalNode *self) {
  delete self;
}

//  QString UniversalNode::createNodeString(int namespaceIndex, const QString
//      &nodeIdentifier)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13UniversalNode16createNodeStringEiRK7QString(
    int namespaceIndex,
    const QString *nodeIdentifier) {
  return new QString(
      UniversalNode::createNodeString(namespaceIndex, *nodeIdentifier));
}

#endif  // !defined(Q_OS_QNX) && !defined(Q_OS_WASM)
