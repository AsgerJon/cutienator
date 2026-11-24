//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSSGCommand::QSSGCommand(CommandType inType)
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN11QSSGCommandC1E11CommandType(CommandType inType) {
  return new QSSGCommand(inType);
}

//  QSSGCommand::~QSSGCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGCommandD1Ev(QSSGCommand *self) {
  delete self;
}

//  const char *QSSGCommand::typeAsString() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QSSGCommand12typeAsStringEv(
    const QSSGCommand *self) {
  return self->typeAsString();
}

//  QString QSSGCommand::debugString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QSSGCommand11debugStringEv(const QSSGCommand *self) {
  return new QString(self->debugString());
}
