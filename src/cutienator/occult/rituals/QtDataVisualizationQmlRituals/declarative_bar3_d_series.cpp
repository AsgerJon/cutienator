//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  declarativeseries_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class
//  line has no export macro. Written: its virtual functions, called
//  through the object: metaObject() and the destructor.
//  Not written: the constructor and 'tr'; the signals; and the
//  slots and the other functions that are not virtual, which Qt's
//  library offers not, 'seriesChildren' and the static
//  'append...' among them.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/declarativeseries_p.h>

//  const QMetaObject *DeclarativeBar3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22DeclarativeBar3DSeries10metaObjectEv(
    const DeclarativeBar3DSeries *self) {
  return self->metaObject();
}

//  DeclarativeBar3DSeries::~DeclarativeBar3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN22DeclarativeBar3DSeriesD1Ev(DeclarativeBar3DSeries *self) {
  delete self;
}
